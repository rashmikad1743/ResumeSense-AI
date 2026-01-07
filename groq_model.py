from groq import Groq
import os
from dotenv import load_dotenv

# Load .env if present (non-fatal if missing)
load_dotenv()

def _get_api_key():
    # Prefer Streamlit secrets if available, else environment/.env
    key = None
    try:
        import streamlit as st
        key = st.secrets.get("GROQ_API_KEY")
    except Exception:
        key = None

    if not key:
        key = os.environ.get("GROQ_API_KEY")

    return key

def get_groq_response(prompt):
    print("USING MODEL: llama-3.1-8b-instant")  # debug

    api_key = _get_api_key()
    if not api_key:
        raise RuntimeError(
            "Missing GROQ_API_KEY. Set it via Streamlit secrets, .env, or environment variable."
        )

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an expert resume reviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=800
    )

    return response.choices[0].message.content
