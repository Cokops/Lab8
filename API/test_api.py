# ТЕСТЫ: TDD подход - сначала тесты
from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_create_task():
    """Тест создания задачи - ИСПРАВЛЕННАЯ ВЕРСИЯ"""
    response = client.post(
        "/tasks/",
        json={"title": "Купить молоко", "description": "2.5%"}
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["title"] == "Купить молоко"
    assert data["description"] == "2.5%"
    assert data["completed"] == False
    assert "id" in data

def test_get_all_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert isinstance(tasks, list)
    assert len(tasks) > 0

def test_get_task_by_id():
    create_response = client.post("/tasks/", json={"title": "Для поиска"})
    task_id = create_response.json()["id"]
    
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Для поиска"

def test_update_task():
    create_response = client.post("/tasks/", json={"title": "Старая"})
    task_id = create_response.json()["id"]
    
    update_response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Новая", "completed": True}
    )
    
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["title"] == "Новая"
    assert data["completed"] == True

def test_delete_task():
    create_response = client.post("/tasks/", json={"title": "Для удаления"})
    task_id = create_response.json()["id"]
    
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404

def test_api_flow():

    response1 = client.post("/tasks/", json={"title": "Тестовая"})
    task_id = response1.json()["id"]
    
    response2 = client.get(f"/tasks/{task_id}")
    assert response2.json()["title"] == "Тестовая"
    
    response3 = client.put(
        f"/tasks/{task_id}",
        json={"completed": True}
    )
    assert response3.json()["completed"] == True
    
    response4 = client.delete(f"/tasks/{task_id}")
    assert response4.status_code == 200