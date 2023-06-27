import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class Answer(BaseModel):
    answer: str
    timestamp: datetime.datetime
    correct: bool


class Question(BaseModel):
    question: str
    correct_answer: str
    your_answers: List[Answer] = []

    def __repr__(self):
        return f"question: {self.question} - answer: {self.correct_answer}"


class QuestionDeck(BaseModel):
    name: str
    description: str
    questions: List[Question] = []

    def __repr__(self):
        return f"deck: {self.name}"

class GetQuestionDecksResponse(BaseModel):
    question_decks: List[QuestionDeck]
