from typing import Any

from pydantic import BaseModel, ConfigDict
from pymongo import MongoClient

from config import DATABASE_NAME, DECK_COLLECTION_NAME, QUESTION_COLLECTION_NAME


class GlobalState(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    client: Any
    db: Any
    deck_collection: Any
    question_collection: Any


def set_db(name: str):
    global db
    global deck_collection
    global question_collection

    db = client[name]
    deck_collection = db[DECK_COLLECTION_NAME]
    question_collection = db[QUESTION_COLLECTION_NAME]

    global_state.db = db
    global_state.deck_collection = deck_collection
    global_state.question_collection = question_collection


client = MongoClient()
db = client[DATABASE_NAME]
deck_collection = db[DECK_COLLECTION_NAME]
question_collection = db[QUESTION_COLLECTION_NAME]

global_state = GlobalState(
    client=client,
    db=db,
    deck_collection=deck_collection,
    question_collection=question_collection
)
