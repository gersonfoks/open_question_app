from typing import Optional, List

from pydantic import BaseModel

from model.question import Question, QuestionDeck, Answer


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




class GetQuestionDecksResponse(BaseModel):
    question_decks: List[QuestionDeck]