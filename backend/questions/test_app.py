import requests

question_deck_name = "temp_test_deck"

request = requests.post(
    'http://localhost:8001/create_deck',
    json={
        "name": question_deck_name,
        "description": "This is a test deck",
        "questions": [{
            "question": "What is the capital of germany?",
            "correct_answer": "Berlin",
        },
            {
                "question": "What is the capital of the Netherlands?",
                "correct_answer": "Amsterdam",
            },
        ]
    }
)
print("first response")
print(request.json())

request = requests.post(
    'http://localhost:8001/add_question',
    json={
        "question_deck_name": question_deck_name,
        "question": "What is the capital of france?",
        "correct_answer": "Paris",
    }
)

print(request.json())

request = requests.get(
    'http://localhost:8001/get_question_decks',

)

print(request.json())

request = requests.delete(
    'http://localhost:8001/delete_question_deck',
    json={
        "name": question_deck_name
    }

)

print(request.json())

request = requests.get(
    'http://localhost:8001/get_question_decks',

)

print(request.json())
