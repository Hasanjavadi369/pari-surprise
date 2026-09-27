from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MESSAGES_FILE = os.path.join(BASE_DIR, "messages.txt")

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/send", methods=["POST"])
def send_message():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"success": False, "error": "empty"}), 400

    if len(message) > 1000:
        return jsonify({"success": False, "error": "too_long"}), 400

    with open(MESSAGES_FILE, "a", encoding="utf-8") as f:
        f.write("\n" + "=" * 50 + "\n")
        f.write("زمان: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write("جواب پری: " + message + "\n")

    return jsonify({"success": True})

app.run(host="0.0.0.0", port=8080)
