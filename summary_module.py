import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def summarize_text(text: str) -> str:
    try:
        prompt = f"""
You are EduGenie, an educational AI assistant.

Summarize the following educational text in simple,
clear language.

Keep the important points and remove unnecessary details.

Text:
{text}
"""

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:
        return f"Error in Summary: {e}"
