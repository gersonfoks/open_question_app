import json
import unittest

from bson import ObjectId
from fastapi.testclient import TestClient
from pymongo import MongoClient

from app import global_state, set_db
from app.main import app
from model.question import Question


client = TestClient(app)


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        set_db("test_database")
        self.global_state = global_state

    def tearDown(self) -> None:
        # Remove the collections to remove any side effects
        self.global_state.db.drop_collection(self.global_state.deck_collection)
        self.global_state.db.drop_collection(self.global_state.question_collection)

    def get_content(self, response):
        return json.loads(response.content.decode())

    def test_add_question(self):
        question = Question(
            question="What is the capital of France?",
            answer="Paris"

        )

        content = self.get_content(client.post('/question/add', content=question.json()))

        self.assertEqual(type(content["id"]), str)

    def test_delete_question(self):
        # First insert the question
        question = Question(
            question="What is the capital of France?",
            answer="Paris"
        )

        content = self.get_content(client.post('/question/add', content=question.json()))
        id = content["id"]

        content = self.get_content(client.post('/question/delete', content=json.dumps({"id": id})))

        self.assertEqual(content, {"body": "success"})
