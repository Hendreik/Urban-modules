# module_16_1.py
"""
Основы Fast Api и маршрутизация"
Цель: научиться создавать базовую маршрутизацию для обработки данных в FastAPI.
uvicorn module_16_1:app --reload
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root() -> dict:
	return {"message": "Главная страница"}


@app.get("/user/admin")
async def read_root() -> dict:
	return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def read_user(user_id: int) -> dict:
	return {"User: ": f"Вы вошли как пользователь № <{user_id}>"}


# "Информация о пользователе. Имя: <username>, Возраст: <age>".
# user?name="Jack"&age=22
@app.get("/user")
async def _user(name: str, age: int) -> dict:
	return {"Информация о пользователе. Имя, Возраст: ": f"user: {name} age: {age}"}
