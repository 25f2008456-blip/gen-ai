from sqlalchemy import Column, Integer, String, Text,Boolean
from src.config.db import Base


class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    is_completed=Column(Boolean, default=False)