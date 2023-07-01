from typing import Any

from bson import ObjectId
from fastapi import APIRouter
from pydantic import BaseModel

from app import global_state
from model.question import QuestionDeck

router = APIRouter()


class CreateDeckResponse(BaseModel):
    id: str


class CreateDeckRequest(BaseModel):
    name: str
    description: str
    question_ids: list[str] = []


@router.post('/decks/create', response_model=CreateDeckResponse)
async def create_deck(request: CreateDeckRequest) -> Any:
    request = request.dict()
    question_deck = QuestionDeck(name=request["name"], description=request["description"],
                                 question_ids=request["question_ids"]
                                 )
    result = global_state.deck_collection.insert_one(question_deck.dict())

    return {"id": str(result.inserted_id)}


# delete
class DeleteDeckRequest(BaseModel):
    id: str


class DeleteDeckResponse(BaseModel):
    body: str


@router.post('/decks/delete', response_model=DeleteDeckResponse)
async def delete_deck(deck_request: DeleteDeckRequest) -> Any:
    deck_request = deck_request.dict()

    id = deck_request["id"]

    response = global_state.deck_collection.find_one_and_delete({"_id": ObjectId(id)})

    return {"body": "success"}


# get all
class GetDecksResponse(BaseModel):
    decks: list[QuestionDeck]


@router.get('/decks/get', response_model=GetDecksResponse)
async def get_decks() -> Any:
    decks = global_state.deck_collection.find()
    decks = [QuestionDeck(**deck) for deck in decks]

    return {"decks": decks}
