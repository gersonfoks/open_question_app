from dataclasses import asdict
from typing import Any

import fastapi

from fastapi.middleware.cors import CORSMiddleware

from model.question import Question, QuestionDeck, GetQuestionDecksResponse
from requests_responses import AddQuestionResponse, AddQuestionDeckRequest, AddQuestionRequest, \
    DeleteQuestionDeckResponse, DeleteQuestionDeckRequest

# Load the database collection
from utils import collection

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


@app.post('/create_deck', response_model=AddQuestionResponse)
async def create_deck(request: AddQuestionDeckRequest) -> Any:
    print(request)
    request = request.dict()
    question_deck = QuestionDeck(name=request["name"], description=request["description"])
    collection.insert_one(question_deck.dict())

    return {"body": "question deck created"}


@app.post('/add_question', response_model=AddQuestionResponse)
async def add_question(question_request: AddQuestionRequest) -> Any:
    question_request = question_request.dict()

    question = Question(**question_request)
    collection.find_one_and_update({"name": question_request["question_deck_name"]},
                                   {"$push": {"questions": question.dict()}}
                                   )

    return {"body": f"Question added to {question_request['question_deck_name']}"}


@app.get('/get_question_decks', response_model=GetQuestionDecksResponse)
async def get_question_decks() -> Any:
    question_decks = collection.find()
    question_decks = [QuestionDeck(**question_deck) for question_deck in question_decks]

    return {"question_decks": question_decks}


@app.delete('/delete_question_deck', response_model=DeleteQuestionDeckResponse)
async def get_question_decks(delete_request: DeleteQuestionDeckRequest) -> Any:
    collection.delete_one({"name": delete_request.name})

    return {"body": f"Question deck {delete_request.name} deleted"}

