from dotenv import load_dotenv
load_dotenv()

import requests
import os
import streamlit as st

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY and hasattr(st, "secrets"):
    OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY", None)
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in .env or Streamlit secrets.")
print("DEBUG API KEY:", OPENROUTER_API_KEY)

def generate_response(user_input):
    api_url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3-70b-instruct",
        "messages": [
            {"role": "system", "content": (
                "You are a mental wellness chatbot designed to provide supportive and empathetic responses. "
                "Your goal is to help users feel heard and understood, offering advice and resources when appropriate. "
                "Always prioritize the user's emotional well-being and provide responses that are compassionate and non-judgmental."
                "Please keep your responses brief and to the point, using 2-4 sentences."
            )},
            {"role": "user", "content": user_input}
        ]
    }
    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        print("DEBUG API RESPONSE:", response.json())
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("DEBUG API ERROR:", e)
        try:
            print("DEBUG API RESPONSE (error):", response.json())
        except Exception:
            pass
        return "Sorry, I'm having trouble responding right now. Please try again later."
    
