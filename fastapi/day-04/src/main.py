from fastapi import FastAPI
from src.config.db import Base,engine
Base.metadata.create_all(engine)
app=FastAPI()
app.get('/')
def root():
    return{"message":"hello,from fastapi"}


