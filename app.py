import numpy as np
import streamlit as st
import json
from sentence_transformers import SentenceTransformer

from torch.nn import CosineSimilarity

st.title('Automatic grading example')

@st.cache_data
def get_data():
    with open('questions_with_answers.json') as f:
        data = json.load(f)
    return data

data = get_data()


def get_new_question(data):
    questions = data["questions"]
    random_index = np.random.choice(len(questions))
    question = questions[random_index]
    correct_answer = question["correct_answer"]

    return question["question"], correct_answer

@st.cache_data
def load_models():
    models = [
        SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2'),
        SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2'),
        SentenceTransformer('sentence-transformers/all-distilroberta-v1'),

    ]

    return models


def score_answer_with_model(example_answer, your_answer, model):
    cosine_sim = CosineSimilarity()
    embedded_example_answer = model.encode([example_answer], convert_to_tensor=True)
    embedded_your_answer = model.encode([your_answer], convert_to_tensor=True)

    # Compute cosine-similarities
    cosine_scores = cosine_sim(embedded_your_answer, embedded_example_answer).detach().cpu().numpy()
    return cosine_scores

def score_answer(example_answer, your_answer, models):
    scores = []
    for model in models:
        scores.append(score_answer_with_model(example_answer, your_answer, model))

    return np.mean(scores), np.var(scores)

models = load_models()


if 'question' not in st.session_state:
    st.session_state['question'], st.session_state['correct_answer'] = get_new_question(data)



correct_answer = st.session_state['correct_answer']
question = st.session_state['question']

st.text("Question: " + question)

your_answer = st.text_input('Answer:')

if st.button('Submit'):
    st.write('Your answer is: ', your_answer)
    st.write('Correct answer is: ', correct_answer)

    score = score_answer(correct_answer, your_answer, models)
    st.write('Your score is: ', score)


if st.button('refresh_question'):
    st.session_state['question'], st.session_state['correct_answer'] = get_new_question(data)
