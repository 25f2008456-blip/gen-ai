from fastapi import FastAPI
from src.config.db import Base,engine
from src.tasks.routes import task_Routes
from src.tasks.models import TaskModel
Base.metadata.create_all(engine)
app=FastAPI()

app.include_router(task_Routes)