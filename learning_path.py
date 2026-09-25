import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def get_learning_recommendations(topic: str) -> str:
    try:
        prompt = f"""
You are EduGenie, an AI learning assistant.

Create a structured learning path for the topic below.

Topic:
{topic}

Include:

1. Beginner level
2. Intermediate level
3. Advanced level
4. Important topics to learn at each level
5. Useful learning resources
6. A simple step-by-step learning order

Keep the explanation clear and student-friendly.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Error in Learning Path: {e}"
