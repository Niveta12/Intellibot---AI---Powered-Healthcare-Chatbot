from flask import Flask, render_template, request
from chatbot import query_llm
import json
import os
from datetime import datetime

app = Flask(__name__)
CHAT_LOG_DIR = "chat_logs"

# Ensure log directory exists
os.makedirs(CHAT_LOG_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input:
            response = query_llm(user_input, [])
            # Save chat to file
            save_chat(user_input, response)
    return render_template("index.html", response=response)

def save_chat(user_input, response):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_entry = {
        "timestamp": timestamp,
        "user": user_input,
        "bot": response
    }
    file_path = os.path.join(CHAT_LOG_DIR, f"chat_{timestamp}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(log_entry, f, indent=4)
