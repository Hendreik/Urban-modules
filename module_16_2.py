# module_16_2.py
"""
Задача "Аннотация и валидация":
"""
from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def read_root() -> dict:
	return {"root": "Главная страница"}


@app.get("/user")
async def user_root() -> dict:
	return {"страница": "user"}


"""
'/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id, для которого необходимо написать следующую валидацию:
Должно быть целым числом
Ограничено по значению: больше или равно 1 и меньше либо равно 100.
Описание - 'Enter User ID'
Пример - '1'

uvicorn module_16_2:app --reload
"""


@app.get("/user/{user_id}")
async def read_user(
user_id: int = Path(..., title='Enter User ID', ge=1, le=100, description='only positive integer 1...100',example=1)
):
	return {"User: ": f"Вы вошли как пользователь № <{user_id}>"}


# '/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту, принимает аргументы username и
# age, для которых необходимо написать следующую валидацию:
# username - строка, age - целое число.
# username ограничение по длине: больше или равно 5 и меньше либо равно 20.
# age ограничение по значению: больше или равно 18 и меньше либо равно 120.
# Описания для username и age - 'Enter username' и 'Enter age' соответственно.
# Примеры для username и age - 'UrbanUser' и '24' соответственно. (можете подставить свои примеры не противоречащие валидации).
@app.get("/user/{username}/{age}")
async def _user(
username: Annotated[str, Path(..., min_length=5, max_length=20, regex="^[A-Za-z\\s]+$", title='Enter username',
description='Enter username in english', example='UrbanUser')],
age: Annotated[int, Path(..., ge=18, le=120, title='Enter age',
description="Enter age. only positive integer 18—120 ", example=20)]
):
	"""
	Выводим пользователя.
	- **name**: логин
	- **age**: возраст

	"""
	return {"Информация о пользователе. Имя, Возраст: ": f"user: {username}, age: {age}"}


if __name__ == "__main__":
	import uvicorn

	uvicorn.run(app, host="localhost", port=8001)
