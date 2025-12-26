import uuid
from datetime import datetime

class Task:
    """Модель задачи - данные и бизнес-логика"""
    
    def __init__(self, title: str, description: str = ""):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now()
    
    def complete(self) -> None:
        """Отметить задачу как выполненную"""
        self.completed = True
    
    def update(self, title: str = None, description: str = None) -> None:
        """Обновить данные задачи"""
        if title:
            self.title = title
        if description is not None:
            self.description = description
    
    def to_dict(self) -> dict:
        """Преобразовать в словарь для передачи"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }