import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "put your chat completions url" #for example: "https://api.com/openai/chat/completions"
MODEL = "llama-3.3-70b-versatile"

def query_llm_groq(prompt, chat_history=[]):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [{"role": "system", "content": "You are a helpful and knowledgeable healthcare assistant."}]
    messages += chat_history
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.3
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"GROQ API Error: {response.status_code}"
