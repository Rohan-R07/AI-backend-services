from fastapi import FastAPI
from ai import AiServices

from schema import AiResponseSchema


import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
MODEL_LINK = os.getenv("MODEL_LINK")

app = FastAPI()
obj = AiServices(API_KEY,MODEL_LINK)
obj.setup()


@app.get("/")
def basic():
    return "AI Servises have been initialized"


@app.post("/giveData/{id}",response_model=AiResponseSchema)
def ask_Question(text:str):
    respone = obj.Ask(text)
    return respone
