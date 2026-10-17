import os
import json
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
import anthropic
from knowledge.afs_knowledge import SYSTEM_PROMPT

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))

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

    CONVERSATION_HISTORY[session_id].append({"role": "user", "content": user_message})

    def generate():
        full_response = ""
        with client.messages.stream(
            model="claude-opus-4-5",
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            messages=CONVERSATION_HISTORY[session_id],
        ) as stream:
            for text in stream.text_stream:
                full_response += text
                yield f"data: {json.dumps({'text': text})}\n\n"

        CONVERSATION_HISTORY[session_id].append(
            {"role": "assistant", "content": full_response}
        )
        yield f"data: {json.dumps({'done': True})}\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@app.route("/reset", methods=["POST"])
def reset():
    data = request.json
    session_id = data.get("session_id", "default")
    CONVERSATION_HISTORY.pop(session_id, None)
    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
