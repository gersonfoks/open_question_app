from typing import Any

import fastapi
from pydantic import BaseModel

from grading_model import GradeModel

from fastapi.middleware.cors import CORSMiddleware

origins = [

    "http://localhost:5173",
]



app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize model
grading_model = GradeModel()


class GradeRequest(BaseModel):
    question: str
    correct_answer: str
    your_answer: str


class GradeResponse(BaseModel):
    similarity: float
    correct: bool


@app.post('/grade', response_model=GradeResponse)
async def grade(grade_request: GradeRequest) -> Any:
    grade_request = grade_request.dict()
    question = grade_request["question"]
    correct_answer = grade_request["correct_answer"]
    your_answer = grade_request["your_answer"]
    similarity, correct = grading_model.grade(question, correct_answer, your_answer)

    return {"similarity": similarity, "correct": correct}
