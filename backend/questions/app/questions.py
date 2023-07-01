import datetime
from typing import Any, Optional, List

from bson import ObjectId
from fastapi import APIRouter
from pydantic import BaseModel

from app import global_state
from model.question import Question, Answer

router = APIRouter()


class CreateQuestionRequest(BaseModel):
    question: str
    answer: str
    your_answers: Optional[list[Answer]] = []


class CreateQuestionResponse(BaseModel):
    id: str


@router.post('/question/create', response_model=CreateQuestionResponse)
async def add_question(question_request: CreateQuestionRequest) -> Any:
    question_request = question_request.dict()

    question = Question(**question_request)

    response = global_state.question_collection.insert_one(question.dict())

    return {"id": str(response.inserted_id)}


class DeleteQuestionRequest(BaseModel):
    id: str


class DeleteQuestionResponse(BaseModel):
    body: str


@router.post('/question/delete', response_model=DeleteQuestionResponse)
async def delete_question(question_request: DeleteQuestionRequest) -> Any:
    question_request = question_request.dict()

    id = question_request["id"]

    response = global_state.question_collection.find_one_and_delete({"_id": ObjectId(id)})

    return {"body": "success"}


class AddAnswerRequest(BaseModel):
    question_id: str
    answer: str
    correct: bool


class AddAnswerResponse(BaseModel):
    body: str


@router.post('/question/add_answer', response_model=AddAnswerResponse)
async def delete_question(add_answer_request: AddAnswerRequest) -> Any:
    add_answer_request = add_answer_request.dict()

    id = add_answer_request["question_id"]
    # Add a timestamp
    add_answer_request["timestamp"] = datetime.datetime.now()
    add_answer_request.pop("question_id")
    global_state.question_collection.find_one_and_update({"_id": ObjectId(id)},
                                                         {"$push": {"your_answers": add_answer_request}})

    return {"body": "success"}


class GetQuestionsRequest(BaseModel):
    question_ids: List[str]


class GetQuestionsResponse(BaseModel):
    questions: List[Question]


@router.post('/question/get_questions', response_model=GetQuestionsResponse)
async def delete_question(request: GetQuestionsRequest) -> Any:
    request = request.dict()

    # Add a timestamp
    ids = [ObjectId(id) for id in request["question_ids"]]
    result = global_state.question_collection.find({"_id": {"$in": ids},})

    return {"questions": [Question(**question) for question in result]}
