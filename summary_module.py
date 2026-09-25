import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.6-flash")


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