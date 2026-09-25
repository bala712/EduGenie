import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def explain_topic(topic: str):

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"Explain the topic '{topic}' clearly and simply for a student."
        )

        return response.text

    except Exception as e:
        return f"Error in Explanation: {str(e)}"