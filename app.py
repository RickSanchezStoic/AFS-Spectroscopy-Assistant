import os
import json

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from flask import Flask, render_template, request, jsonify, Response, stream_with_context
import google.generativeai as genai
from knowledge.afs_knowledge import SYSTEM_PROMPT

app = Flask(__name__)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", ""))

CONVERSATION_HISTORY = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    session_id = data.get("session_id", "default")
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    if session_id not in CONVERSATION_HISTORY:
        CONVERSATION_HISTORY[session_id] = []

    CONVERSATION_HISTORY[session_id].append({"role": "user", "parts": [user_message]})

    def generate():
        full_response = ""
        history = CONVERSATION_HISTORY[session_id][:-1][-4:]  # last 2 turns excluding current
        model = genai.GenerativeModel(
            model_name="gemini-3.8-flash",
            system_instruction=SYSTEM_PROMPT,
        )
        chat_session = model.start_chat(history=history)
        stream = chat_session.send_message(user_message, stream=True)
        for chunk in stream:
            text = chunk.text or ""
            if text:
                full_response += text
                yield f"data: {json.dumps({'text': text})}\n\n"

        CONVERSATION_HISTORY[session_id].append({"role": "model", "parts": [full_response]})
        yield f"data: {json.dumps({'done': True})}\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@app.route("/suggest", methods=["POST"])
def suggest():
    data = request.json
    user_message = data.get("user_message", "").strip()
    assistant_response = data.get("assistant_response", "").strip()

    if not user_message or not assistant_response:
        return jsonify({"suggestions": []})

    prompt = (
        "You are helping an AFS spectroscopy expert. "
        "Given the customer enquiry and the assistant's response below, "
        "generate exactly 3 short follow-up questions the user might ask next. "
        "Each question must be specific to spectroscopy or the AFS process — no generic questions. "
        "Return ONLY a JSON array of 3 strings, nothing else.\n\n"
        f"ENQUIRY: {user_message[:500]}\n\n"
        f"RESPONSE SUMMARY: {assistant_response[:800]}"
    )

    try:
        model = genai.GenerativeModel("gemini-3.8-flash")
        response = model.generate_content(prompt)
        raw = response.text.strip()
        start = raw.find("[")
        end = raw.rfind("]") + 1
        suggestions = json.loads(raw[start:end]) if start != -1 else []
        suggestions = [s for s in suggestions if isinstance(s, str)][:3]
    except Exception:
        suggestions = []

    return jsonify({"suggestions": suggestions})


@app.route("/reset", methods=["POST"])
def reset():
    data = request.json
    session_id = data.get("session_id", "default")
    CONVERSATION_HISTORY.pop(session_id, None)
    return jsonify({"ok": True})


@app.route("/rewind", methods=["POST"])
def rewind():
    data = request.json
    session_id = data.get("session_id", "default")
    turn_index = data.get("turn_index", 0)
    if session_id in CONVERSATION_HISTORY:
        CONVERSATION_HISTORY[session_id] = CONVERSATION_HISTORY[session_id][:turn_index * 2]
    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
