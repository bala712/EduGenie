import os
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.6-flash")


def clean_json_block(text: str) -> str:
    text = text.strip()

    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)

    return text.strip()


def generate_quiz(text: str):

    prompt = f"""
You are EduGenie, an educational quiz generator.

Create exactly 3 multiple-choice questions about:
{text}

Return ONLY a valid JSON array.

Use exactly this format:

[
  {{
    "question": "What is photosynthesis?",
    "options": [
      "Process of making food",
      "Process of breathing",
      "Process of digestion",
      "Process of reproduction"
    ],
    "answer": "Process of making food"
  }}
]

Rules:
- Exactly 3 questions
- Exactly 4 options for each question
- The answer must exactly match one option
- Do not add markdown
- Do not add explanations
- Return ONLY JSON
"""

    try:
        response = model.generate_content(prompt)

        raw_text = response.text
        cleaned = clean_json_block(raw_text)

        quiz = json.loads(cleaned)

        if not isinstance(quiz, list):
            raise ValueError("Quiz response is not a list")

        if len(quiz) != 3:
            raise ValueError("Quiz does not contain exactly 3 questions")

        for item in quiz:
            if not isinstance(item, dict):
                raise ValueError("Invalid question format")

            if "question" not in item:
                raise ValueError("Question field missing")

            if "options" not in item:
                raise ValueError("Options field missing")

            if "answer" not in item:
                raise ValueError("Answer field missing")

            if not isinstance(item["options"], list):
                raise ValueError("Options must be a list")

            if len(item["options"]) != 4:
                raise ValueError("Each question must have 4 options")

            if item["answer"] not in item["options"]:
                raise ValueError("Answer does not match an option")

        return quiz

    except Exception as e:
        print("QUIZ ERROR:", repr(e))

        return None