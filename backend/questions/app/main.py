from fastapi import FastAPI

from app import questions, decks

app = FastAPI()

app.include_router(questions.router)
app.include_router(decks.router)