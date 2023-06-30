from typing import Any, Optional

from bson import ObjectId
from fastapi import APIRouter
from pydantic import BaseModel

from app import global_state
from model.question import Question, Answer

router = APIRouter()


class AddQuestionRequest(BaseModel):
    question: str
    answer: str
    your_answers: Optional[list[Answer]] = []


class AddQuestionResponse(BaseModel):
    id: str


class DeleteQuestionRequest(BaseModel):
    id: str


class DeleteQuestionResponse(BaseModel):
    body: str


@router.post('/question/add', response_model=AddQuestionResponse)
async def add_question(question_request: AddQuestionRequest) -> Any:
    question_request = question_request.dict()

    question = Question(**question_request)

    response = global_state.question_collection.insert_one(question.dict())

    return {"id": str(response.inserted_id)}


@router.post('/question/delete', response_model=DeleteQuestionResponse)
async def delete_question(question_request: DeleteQuestionRequest) -> Any:
    question_request = question_request.dict()

    id = question_request["id"]
    
    response = global_state.question_collection.find_one_and_delete({"_id": ObjectId(id)})

    return {"body": "success"}
