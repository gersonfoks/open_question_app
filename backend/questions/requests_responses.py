from pydantic import BaseModel


class AddQuestionDeckRequest(BaseModel):
    name: str


class AddQuestionDeckResponse(BaseModel):
    body: str


class AddQuestionRequest(BaseModel):
    question: str
    correct_answer: str
    question_deck_name: str


class AddQuestionResponse(BaseModel):
    body: str