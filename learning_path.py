import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def get_learning_recommendations(topic: str):
    try:
        prompt = f"""
You are EduGenie, an AI learning assistant.

Create a simple step-by-step learning path for:

Topic: {topic}

Include:

1. Beginner level
2. Intermediate level
3. Advanced level
4. Important topics to learn
5. Useful learning resources
6. Simple learning order

Keep the explanation clear and student-friendly.
"""

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        print("Learning Path Error:", e)
        return f"Error in Learning Path: {str(e)}"
