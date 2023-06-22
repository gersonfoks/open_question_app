import requests


request = requests.post(
    'http://localhost:8001/create_deck',
    json={
        "name": "test_deck"
    }
)



print(request.json())


request = requests.post(
    'http://localhost:8001/add_question',
    json={
        "question_deck_name": "test_deck",
        "question": "What is the capital of france?",
        "correct_answer": "Paris",
    }
)

print(request.json())



request = requests.get(
    'http://localhost:8001/get_question_decks',

)

print(request.json())