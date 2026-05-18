from fastapi import APIRouter
from src.tasks import controllers
task_Routes=APIRouter(prefix='/tasks')

@task_Routes.post("/create")
def create_task():
    return controllers.create_task()