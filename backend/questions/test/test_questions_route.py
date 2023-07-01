import json
import unittest

from bson import ObjectId
from fastapi.testclient import TestClient
from pymongo import MongoClient

from app import global_state, set_db
from app.main import app
from model.question import Question

client = TestClient(app)


class TestQuestionsRoute(unittest.TestCase):

    def setUp(self) -> None:
        set_db("test_database")
        self.global_state = global_state

    def tearDown(self) -> None:
        # Remove the collections to remove any side effects
        self.global_state.db.drop_collection(self.global_state.deck_collection)
        self.global_state.db.drop_collection(self.global_state.question_collection)

    def get_content(self, response):
        return json.loads(response.content.decode())

    def test_create_question(self):
        question = Question(
            question="What is the capital of France?",
            answer="Paris"

        )

        content = self.get_content(client.post('/question/create', content=question.json()))

        self.assertEqual(type(content["id"]), str)

    def test_delete_question(self):
        # First insert the question
        question = Question(
            question="What is the capital of France?",
            answer="Paris"
        )

        content = self.get_content(client.post('/question/create', content=question.json()))
        id = content["id"]

        content = self.get_content(client.post('/question/delete', content=json.dumps({"id": id})))

        # Check if the question is deleted
        self.assertEqual(self.global_state.question_collection.find_one({"_id": ObjectId(id)}), None)

        self.assertEqual(content, {"body": "success"})

    def test_add_answer(self):
        # First insert the question
        question = Question(
            question="What is the capital of France?",
            answer="Paris"
        )

        content = self.get_content(client.post('/question/create', content=question.json()))
        id = content["id"]

        answer = {
            "question_id": id,
            "answer": "Paris",
            "correct": True
        }

        content = self.get_content(client.post('/question/add_answer', content=json.dumps(
            answer
        )))

        self.assertEqual(content, {"body": "success"})

        # Check if the answer is added together with the timestamp
        question = self.global_state.question_collection.find_one({"_id": ObjectId(id)})
        self.assertEqual(question["your_answers"][0]["answer"], "Paris")
        self.assertEqual(question["your_answers"][0]["correct"], True)
        self.assertIn("timestamp", question["your_answers"][0])

    def test_get_questions(self):
        questions = [
            Question(
                question="What is the capital of France?",
                answer="Paris"
            ),
            Question(
                question="What is the capital of Germany?",
                answer="Berlin"
            ),
            Question(
                question="What is the capital of Italy?",
                answer="Rome"
            )
        ]
        ids = []
        for question in questions:
            content = self.get_content(client.post('/question/create', content=question.json()))
            id = content["id"]
            ids.append(id)

        content = self.get_content(client.post('/question/get_questions', content=json.dumps({
            "question_ids": ids
        })))

        # Simply check if the questions are returned
        self.assertEqual(len(content["questions"]), 3)
