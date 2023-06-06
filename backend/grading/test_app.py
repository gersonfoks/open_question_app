import requests


request = requests.post(
    'http://localhost:8000/grade',
    json={
        "question": "What is the capital of France?",
        "correct_answer": "Paris",
        "your_answer": "Paris"
    }
)

print(request.json())

