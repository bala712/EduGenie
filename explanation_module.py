import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def explain_topic(topic: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are EduGenie, an educational AI assistant.

Explain the following topic in simple, clear and student-friendly language.

Topic:
{topic}

Include:
1. Simple definition
2. Important points
3. Easy example
4. Real-world application
5. Short summary

Make the explanation easy for students to understand.
"""
        )

        return response.text.strip()

    except Exception as e:
        return "AI service is temporarily busy. Please try again in a few seconds."
