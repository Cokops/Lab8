from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    """Схема для создания задачи"""
    title: str
    description: Optional[str] = ""

class TaskUpdate(BaseModel):
    """Схема для обновления задачи"""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskResponse(BaseModel):
    """Схема для ответа API"""
    id: str
    title: str
    description: str
    completed: bool
    created_at: str