import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def answer_question(question: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=f"""
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and simply.

Question:
{question}

Give a helpful and easy-to-understand answer.
"""
        )

        return response.text.strip()

    except Exception as e:
        return f"Error: {str(e)}"
