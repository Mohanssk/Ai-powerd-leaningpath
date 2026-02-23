from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import requests

app = Flask(__name__)
CORS(app)

# ======================================
# LOAD ROADMAP DATA
# ======================================
with open("roadmaps_master.json", "r", encoding="utf-8") as f:
    ROADMAPS = json.load(f)

# ======================================
# OPENROUTER API
# ======================================
OPENROUTER_API_KEY = "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"

# ======================================
# NORMALIZE SKILL
# ======================================
def normalize_skill(skill):
    return skill.lower().replace(" ", "-").replace("_", "-")

# ======================================
# AUTO CERT ENGINE
# ======================================
def generate_free_certs(topic):

    q = topic.replace(" ", "%20")

    return [
        {
            "title": f"freeCodeCamp - {topic}",
            "url": f"https://www.freecodecamp.org/news/search/?query={q}"
        },
        {
            "title": f"Coursera Free Courses - {topic}",
            "url": f"https://www.coursera.org/search?query={q}&price=free"
        },
        {
            "title": f"edX Free Courses - {topic}",
            "url": f"https://www.edx.org/search?q={q}&price=free"
        },
        {
            "title": f"Google Digital Garage - {topic}",
            "url": f"https://learndigital.withgoogle.com/digitalgarage/search?q={q}"
        },
        {
            "title": f"Kaggle Learn - {topic}",
            "url": f"https://www.kaggle.com/search?q={q}"
        }
    ]

# ======================================
# ROOT
# ======================================
@app.route("/")
def home():
    return jsonify({"status": "Backend Running 🚀"})

# ======================================
# GET ALL SKILLS
# ======================================
@app.route("/skills", methods=["GET"])
def skills():
    return jsonify(list(ROADMAPS.keys()))

# ======================================
# GENERATE ROADMAP
# ======================================
@app.route("/generate", methods=["POST"])
def generate():

    data = request.json
    skill = normalize_skill(data.get("skill", ""))

    if skill not in ROADMAPS:
        return jsonify({"error": "Skill not found"})

    roadmap = ROADMAPS[skill]

    print("ROADMAP GENERATED:", skill)

    return jsonify({
        "roadmap": roadmap
    })

# ======================================
# NODE CERTIFICATIONS
# ======================================
@app.route("/node-certs", methods=["POST"])
def node_certs():

    node = request.json.get("node", "")

    certs = generate_free_certs(node)

    print("NODE CERT REQUEST:", node)

    return jsonify({
        "certifications": certs
    })

# ======================================
# OPENROUTER REQUEST HELPER
# ======================================
def ask_openrouter(messages):

    if not OPENROUTER_API_KEY:
        return "AI not configured. Add OPENROUTER_API_KEY."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": messages
    }

    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )

        result = r.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return str(e)

# ======================================
# AI NODE EXPLAINER
# ======================================
@app.route("/explain", methods=["POST"])
def explain():

    topic = request.json.get("topic", "")

    explanation = ask_openrouter([
        {
            "role": "system",
            "content":
            "Explain in sections: What it is, Why important, How to learn, Time required."
        },
        {
            "role": "user",
            "content": topic
        }
    ])

    return jsonify({"explanation": explanation})

# ======================================
# CHATBOT
# ======================================
@app.route("/chat", methods=["POST"])
def chat():

    question = request.json.get("question", "")

    reply = ask_openrouter([
        {"role": "system", "content": "You are an AI learning mentor."},
        {"role": "user", "content": question}
    ])

    return jsonify({"reply": reply})

# ======================================
# RUN APP
# ======================================
if __name__ == "__main__":
    app.run(debug=True)