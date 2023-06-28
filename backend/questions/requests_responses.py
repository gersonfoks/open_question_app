from typing import Optional

from pydantic import BaseModel

from model.question import Question


class AddQuestionDeckRequest(BaseModel):
    name: str
    description: str
    questions: Optional[list[Question]] = []


class AddQuestionDeckResponse(BaseModel):
    body: str


class DeleteQuestionDeckRequest(BaseModel):
    name: str


class DeleteQuestionDeckResponse(BaseModel):
    body: str


class AddQuestionRequest(BaseModel):
    question: str
    correct_answer: str
    question_deck_name: str


class AddQuestionResponse(BaseModel):
    body: str
