from dotenv import load_dotenv
load_dotenv()

import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # Set this in your environment for security

def generate_response(user_input):
    api_url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3-70b-instruct",  # Or any supported model
        "messages": [
            {"role": "system", "content": (
                "You are a mental wellness chatbot designed to provide supportive and empathetic responses. "
                "Your goal is to help users feel heard and understood, offering advice and resources when appropriate. "
                "Always prioritize the user's emotional well-being and provide responses that are compassionate and non-judgmental."
                "Please keep your responses brief and to the point, using 2-4 sentences."
                
                )
            },
            {"role": "user", "content": user_input}
        ]
    }
    response = requests.post(api_url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()