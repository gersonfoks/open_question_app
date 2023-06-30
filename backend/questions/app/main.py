from fastapi import FastAPI

from app import questions

app = FastAPI()

app.include_router(questions.router)