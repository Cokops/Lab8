from fastapi import FastAPI
from controller_api import router as tasks_router
import uvicorn

app = FastAPI(
    title="ToDo API",
    description="Простое ToDo приложение с MVC архитектурой",
    version="1.0.0"
)

app.include_router(tasks_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)