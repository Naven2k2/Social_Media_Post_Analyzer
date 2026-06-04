import os
from dotenv import load_dotenv
from google import genai

# Load .env for local development
load_dotenv()

# Try .env first
api_key = os.getenv("GEMINI_API_KEY")

# If not found, try Streamlit Secrets
if not api_key:
    try:
        import streamlit as st
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        raise ValueError(
            "GEMINI_API_KEY not found in .env or Streamlit Secrets."
        )

client = genai.Client(api_key=api_key)


def get_response(prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    return response.text