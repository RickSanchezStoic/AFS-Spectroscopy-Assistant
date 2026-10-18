import os
import json

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from knowledge.afs_knowledge import SYSTEM_PROMPT

app = Flask(__name__)

# ── Provider selection ──────────────────────────────────────────────────────
# Change this ONE line to switch providers.
# Options: "claude" | "groq" | "gemini" | "sambanova"
#
# RECOMMENDED FOR DEMO: "claude" (claude-haiku-4-5)
#   → Best response quality; requires ANTHROPIC_API_KEY in .env
#
# DEFAULT / FALLBACK: "groq" (free tier, fast)
#   → Requires GROQ_API_KEY in .env; free at console.groq.com
PROVIDER = "groq"

if PROVIDER == "claude":
    import anthropic
    _client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))
    MODEL = "claude-haiku-4-5"

elif PROVIDER == "sambanova":
    from openai import OpenAI
    _client = OpenAI(
        base_url="https://api.sambanova.ai/v1",
        api_key=os.environ.get("SAMBANOVA_API_KEY", ""),
    )
    MODEL = "Meta-Llama-3.3-70B-Instruct"

elif PROVIDER == "groq":
    from groq import Groq
    _client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))
    MODEL = "openai/gpt-oss-120b"
    _suggest_client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))
    SUGGEST_MODEL = "llama-3.1-8b-instant"

elif PROVIDER == "gemini":
    import google.generativeai as genai
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY", ""))
    _client = None
    MODEL = "gemini-3.8-flash"

print(f"[AFS] Provider: {PROVIDER.title()} / {MODEL}")
# ───────────────────────────────────────────────────────────────────────────

CONVERSATION_HISTORY = {}


def _chat_stream(history, user_message):
    if PROVIDER == "claude":
        messages = []
        for turn in history:
            role = "assistant" if turn["role"] == "model" else turn["role"]
            messages.append({"role": role, "content": turn["parts"][0]})
        messages.append({"role": "user", "content": user_message})
        with _client.messages.stream(
            model=MODEL, system=SYSTEM_PROMPT, messages=messages, max_tokens=4096
        ) as stream:
            for text in stream.text_stream:
                yield text or ""
    elif PROVIDER in ("sambanova", "groq"):
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for turn in history:
            role = "assistant" if turn["role"] == "model" else turn["role"]
            messages.append({"role": role, "content": turn["parts"][0]})
        messages.append({"role": "user", "content": user_message})
        stream = _client.chat.completions.create(
            model=MODEL, messages=messages, stream=True, max_tokens=4096
        )
        for chunk in stream:
            yield chunk.choices[0].delta.content or ""
    else:  # gemini
        model = genai.GenerativeModel(model_name=MODEL, system_instruction=SYSTEM_PROMPT)
        chat_session = model.start_chat(history=history)
        for chunk in chat_session.send_message(user_message, stream=True):
            yield chunk.text or ""


def _suggest_once(prompt):
    if PROVIDER == "claude":
        resp = _client.messages.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=256,
        )
        return resp.content[0].text.strip()
    elif PROVIDER == "groq":
        resp = _suggest_client.chat.completions.create(
            model=SUGGEST_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=256,
        )
        return resp.choices[0].message.content.strip()
    elif PROVIDER == "sambanova":
        resp = _client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=256,
        )
        return resp.choices[0].message.content.strip()
    else:  # gemini
        return genai.GenerativeModel(MODEL).generate_content(prompt).text.strip()


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
        history = CONVERSATION_HISTORY[session_id][:-1][-4:]
        try:
            for text in _chat_stream(history, user_message):
                if text:
                    full_response += text
                    yield f"data: {json.dumps({'text': text})}\n\n"
        except Exception as e:
            err = str(e)
            if "quota" in err.lower() or "rate" in err.lower() or "429" in err:
                msg = "⚠️ Rate limit reached. Wait a moment or switch PROVIDER in app.py."
            elif "404" in err:
                msg = "⚠️ Model not found. Check the MODEL name in app.py."
            else:
                msg = f"⚠️ API error: {err[:200]}"
            yield f"data: {json.dumps({'text': msg})}\n\n"
            full_response = msg

        if not full_response:
            msg = "⚠️ No response received. API may be unavailable."
            yield f"data: {json.dumps({'text': msg})}\n\n"
            full_response = msg

        CONVERSATION_HISTORY[session_id].append({"role": "model", "parts": [full_response]})
        yield f"data: {json.dumps({'done': True})}\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
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
        f"ENQUIRY: {user_message[:500]}\n\nRESPONSE SUMMARY: {assistant_response[:800]}"
    )
    try:
        raw = _suggest_once(prompt)
        start, end = raw.find("["), raw.rfind("]") + 1
        suggestions = json.loads(raw[start:end]) if start != -1 else []
        suggestions = [s for s in suggestions if isinstance(s, str)][:3]
    except Exception:
        suggestions = []
    return jsonify({"suggestions": suggestions})


@app.route("/reset", methods=["POST"])
def reset():
    session_id = request.json.get("session_id", "default")
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
