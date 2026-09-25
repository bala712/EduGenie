from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from qna import answer_question
from explanation_module import explain_topic
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import get_learning_recommendations


app = FastAPI(title="EduGenie")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# -----------------------------
# ASK A QUESTION
# -----------------------------

@app.post("/qa")
@app.post("/ask")
async def qa(request: Request):
    try:
        question = ""

        # Try form data
        try:
            form = await request.form()
            question = form.get("question", "")
        except Exception:
            pass

        # Try JSON if form was empty
        if not question:
            try:
                data = await request.json()
                question = data.get("question", "")
            except Exception:
                pass

        # Try query parameter
        if not question:
            question = request.query_params.get("question", "")

        question = str(question).strip()

        if not question:
            return {
                "answer": "Please enter a question."
            }

        result = answer_question(question)

        return {
            "answer": result
        }

    except Exception as e:
        return {
            "answer": f"Error in Answer: {str(e)}"
        }


# -----------------------------
# EXPLAIN TOPIC
# -----------------------------

@app.post("/explain")
async def explain(topic: str):
    try:
        result = explain_topic(topic)

        return {
            "explanation": result
        }

    except Exception as e:
        return {
            "explanation": f"Error in Explanation: {str(e)}"
        }


# -----------------------------
# SUMMARIZE
# -----------------------------

@app.post("/summarize")
async def summarize(text: str):
    try:
        result = summarize_text(text)

        if not result:
            return {
                "summary": "Summary generation failed."
            }

        return {
            "summary": result
        }

    except Exception as e:
        return {
            "summary": f"Error in Summary: {str(e)}"
        }


# -----------------------------
# QUIZ
# -----------------------------

@app.post("/quiz")
async def quiz(text: str):
    try:
        result = generate_quiz(text)

        if not result:
            return {
                "quiz": [],
                "error": "Quiz generation failed."
            }

        return {
            "quiz": result
        }

    except Exception as e:
        return {
            "quiz": [],
            "error": f"Error in Quiz: {str(e)}"
        }


# -----------------------------
# LEARNING PATH
# -----------------------------

@app.post("/learn/recommendations")
async def learning_path(topic: str):
    try:
        result = get_learning_recommendations(topic)

        return {
            "recommendations": result
        }

    except Exception as e:
        return {
            "recommendations": f"Error in Learning Path: {str(e)}"
        }
