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


@app.post("/qa")
async def qa(question: str):
    return {"answer": answer_question(question)}


@app.post("/explain")
async def explain(topic: str):
    return {"explanation": explain_topic(topic)}


@app.post("/summarize")
async def summarize(text: str):
    result = summarize_text(text)

    if not result:
        return {"error": "Summary generation failed"}

    return {"summary": result}


@app.post("/quiz")
async def quiz(text: str):
    result = generate_quiz(text)

    if not result:
        return {
            "quiz": [],
            "error": "Quiz generation failed. Check terminal."
        }

    return {
        "quiz": result
    }


@app.post("/quiz")
async def quiz(text: str):
    return {"quiz": generate_quiz(text)}


@app.post("/learn/recommendations")
async def learning_path(topic: str):
    return {
        "recommendations": get_learning_recommendations(topic)
    }