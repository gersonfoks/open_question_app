from typing import Any

import fastapi
from pydantic import BaseModel

from grading_model import GradeModel

app = fastapi.FastAPI()

# Initialize model
grading_model = GradeModel()


class GradeRequest(BaseModel):
    question: str
    correct_answer: str
    your_answer: str


class GradeResponse(BaseModel):
    simularity: float
    correct: bool


@app.post('/grade', response_model=GradeResponse)
async def grade(grade_request: GradeRequest) -> Any:
    grade_request = grade_request.dict()
    question = grade_request["question"]
    correct_answer = grade_request["correct_answer"]
    your_answer = grade_request["your_answer"]
    simularity, correct = grading_model.grade(question, correct_answer, your_answer)

    return {"simularity": simularity, "correct": correct}
