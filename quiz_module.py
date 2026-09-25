import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_quiz(text: str) -> str:
    try:
        prompt = f"""
You are EduGenie, an educational AI assistant.

Create a quiz from the following educational text.

Give:
1. 5 multiple-choice questions
2. 4 options for each question
3. Correct answer for each question

Keep the questions simple and clear.

Text:
{text}
"""

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Error in Quiz: {e}"
