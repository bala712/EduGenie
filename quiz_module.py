import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_quiz(text: str):
    try:
        prompt = f"""
Create a quiz from the following topic.

Topic:
{text}

Return ONLY valid JSON.
Do not use markdown.
Do not use ```json.

Format exactly like this:

[
  {{
    "question": "What is the capital of India?",
    "options": [
      "Chennai",
      "Mumbai",
      "New Delhi",
      "Kolkata"
    ],
    "answer": "New Delhi"
  }}
]

Create exactly 5 multiple-choice questions.
Each question must have 4 options.
Give the correct answer.
"""

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        result = response.text.strip()

        # Remove markdown if Gemini adds it
        if result.startswith("```"):
            result = result.replace("```json", "")
            result = result.replace("```", "")
            result = result.strip()

        quiz = json.loads(result)

        if not isinstance(quiz, list):
            return []

        return quiz

    except Exception as e:
        print("Quiz Error:", e)
        return []
