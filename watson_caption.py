import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WATSON_API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
DEPLOYMENT_ID = os.getenv("GENAI_DEPLOYMENT_ID")
WATSON_URL = os.getenv("WATSON_ENDPOINT")

def generate_caption(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    body = {
        "input": prompt,
        "parameters": {
            "decoding_method": "sample",
            "max_new_tokens": 60,
            "temperature": 0.8,
            "top_k": 50,
            "top_p": 0.95,
        },
        "project_id": PROJECT_ID,
    }

    response = requests.post(
        f"{WATSON_URL}/ml/v1/text/generation?deployment_id={DEPLOYMENT_ID}",
        headers=headers,
        json=body
    )

    if response.status_code == 200:
        return response.json().get("results", [{}])[0].get("generated_text", "").strip()
    else:
        print("Error:", response.text)
        return "⚠️ Watsonx.ai failed to generate caption."
