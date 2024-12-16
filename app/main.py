# Структура проекта. Маршруты и модели Pydantic.
"""
Задача "Основные маршруты":
Необходимо создать маршруты и написать Pydantic модели для дальнейшей работы.
В файле main.py создайте сущность FastAPI(), напишите один маршрут для неё - '/', по которому функция возвращает
 словарь - {"message": "Welcome to Taskmanager"}.
Импортируйте объекты APIRouter и подключите к ранее созданному приложению FastAPI, объединив все маршруты в одно
 приложение.
"""
from fastapi import FastAPI
from fastapi import APIRouter
from routers import user
import routers.task as task

#import backend.db as db

router= APIRouter()
app = FastAPI()

@app.get("/")
async def main():
	return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

@app.get("/main")
async def main():
	return {"main":"Shop"}



if __name__=="__main__":
	import uvicorn

	import app.backend.db as db
	print(__name__)
	db.Base.metadata.create_all(bind=db.engine)

"""
cd app
uvicorn main:app --reload
"""
"""
alembic revision --autogenerate -m "init migration"

alembic upgrade head
"""













































