import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

url = "https://api.openai.com/v1/chat/completions"


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}",
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": "Pfv, qual a capital da França?",
        }
    ],
    "temperature": 0.5,
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json()["choices"][0]["message"]["content"], "\n\n")
except Exception:
    print("Ocorreu um erro ao fazer a requisição")
    print(response.json()["error"]["message"])
