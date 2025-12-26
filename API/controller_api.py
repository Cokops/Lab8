# КОНТРОЛЛЕР: управление логикой приложения
from fastapi import APIRouter, HTTPException
from model_task import Task
from view_schemas import TaskCreate, TaskUpdate, TaskResponse
from typing import List

# Хранилище задач (вместо БД)
tasks_db = []

# Создаем роутер
router = APIRouter(prefix="/tasks", tags=["tasks"])

def _find_task(task_id: str) -> Task:
    """Найти задачу по ID"""
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")

@router.post("/", response_model=TaskResponse)
def create_task(task_data: TaskCreate):
    """Создать новую задачу"""
    task = Task(title=task_data.title, description=task_data.description)
    tasks_db.append(task)
    return task.to_dict()

@router.get("/", response_model=List[TaskResponse])
def get_all_tasks():
    """Получить все задачи"""
    return [task.to_dict() for task in tasks_db]

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: str):
    """Получить задачу по ID"""
    task = _find_task(task_id)
    return task.to_dict()

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: str, task_data: TaskUpdate):
    """Обновить задачу"""
    task = _find_task(task_id)
    
    if task_data.title:
        task.title = task_data.title
    if task_data.description is not None:
        task.description = task_data.description
    if task_data.completed is not None:
        task.completed = task_data.completed
    
    return task.to_dict()

@router.delete("/{task_id}")
def delete_task(task_id: str):
    """Удалить задачу"""
    task = _find_task(task_id)
    tasks_db.remove(task)
    return {"message": "Задача удалена"}