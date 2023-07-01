import json
import unittest

from bson import ObjectId
from fastapi.testclient import TestClient

from app import global_state, set_db
from app.main import app


client = TestClient(app)


class TestDecksRoute(unittest.TestCase):

    def setUp(self) -> None:
        set_db("test_database")
        self.global_state = global_state

    def tearDown(self) -> None:
        # Remove the collections to remove any side effects
        self.global_state.db.drop_collection(self.global_state.deck_collection)
        self.global_state.db.drop_collection(self.global_state.question_collection)

    def get_content(self, response):
        return json.loads(response.content.decode())

    def test_create_deck(self):
        content = self.get_content(client.post('/decks/create', content=json.dumps(
            {"name": "test_deck", "description": "test_description", "question_ids": []})))

        self.assertEqual(type(content["id"]), str)

    def test_delete_deck(self):
        # First insert the deck
        content = self.get_content(client.post('/decks/create', content=json.dumps(
            {"name": "test_deck", "description": "test_description", "question_ids": []})))
        id = content["id"]

        content = self.get_content(client.post('/decks/delete', content=json.dumps({"id": id})))

        # Check if the deck is deleted
        self.assertEqual(self.global_state.deck_collection.find_one({"_id": ObjectId(id)}), None)

        self.assertEqual(content, {"body": "success"})

    def test_get_decks(self):
        # First insert multiple decks

        decks = [
            {"name": "test_deck", "description": "test_description", "question_ids": []},
            {"name": "test_deck2", "description": "test_description2", "question_ids": []},
            {"name": "test_deck3", "description": "test_description3", "question_ids": []}
        ]

        # insert the decks
        for deck in decks:
            content = self.get_content(client.post('/decks/create', content=json.dumps(deck)))

        content = self.get_content(client.get('/decks/get'))

        # Check if the decks are returned
        self.assertEqual(content, {"decks": decks})
