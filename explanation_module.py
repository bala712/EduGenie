import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def explain_topic(topic: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=f"""
You are EduGenie, an educational AI assistant.

Explain the following topic in simple,
clear and student-friendly language.

Topic:
{topic}

Include:
- Simple definition
- Important points
- Easy example
"""
        )

        return response.text.strip()

    except Exception as e:
        return f"Error in Explanation: {str(e)}"
