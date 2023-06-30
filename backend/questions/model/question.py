import datetime
from typing import List, Optional

from pydantic import BaseModel


class Answer(BaseModel):
    answer: str
    timestamp: datetime.datetime
    correct: bool


class Question(BaseModel):
    question: str
    answer: str
    your_answers: List[Answer] = []

    def __repr__(self):
        return f"question: {self.question} - answer: {self.answer}"


class QuestionDeck(BaseModel):
    name: str
    description: str
    # The ids of the questions in the question deck
    question_ids: List[str] = []

    def __repr__(self):
        return f"deck: {self.name}"
