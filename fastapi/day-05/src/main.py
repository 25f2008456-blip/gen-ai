from fastapi import FastAPI
from src.config.db import Base,engine
from src.tasks.models import TaskModel
Base.metadata.create_all(engine)
app=FastAPI()

@app.get("/")
def root():
    return{"hello,from fastapi"}