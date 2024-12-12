# module_16_3.py
"""
Задача "Имитация работы с БД":
Создайте новое приложение FastAPI и сделайте CRUD запросы.
Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
Реализуйте 4 CRUD запроса:
get запрос по маршруту '/users', который возвращает словарь users.
post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по значению ключом значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users под ключом user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is updated"
delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
1. GET '/users'
{
"1": "Имя: Example, возраст: 18"
}
2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
"User 2 is registered"
3. POST '/user/{username}/{age}' # username - NewUser, age - 22
"User 3 is registered"
4. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
"User 1 has been updated"
5. DELETE '/user/{user_id}' # user_id - 2
"User 2 has been deleted"
6. GET '/users'
{
"1": "Имя: UrbanProfi, возраст: 28",
"3": "Имя: NewUser, возраст: 22"
}
"""
from typing import Annotated
from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

@app.get("/")
async def read_root() -> dict:
	return {"root": "Главная страница"}

users = {'1': 'Имя: Example, возраст: 18'}
users.update({'2':'ququ'})

@app.get("/users")
async def get_users():
	return users

#http://127.0.0.1:8000/users/1
@app.get("/users/{user_id}")
async def get_user(user_id: str):
	for key in users:
		if key == user_id:
			return {key: users[key]}
	raise HTTPException(status_code=404, detail="Задача не найдена")

@app.post("/{username}/{age}")
async def create_user(username: str,age: Annotated[
	int, Path(ge=18, le=120, title='Enter age', description="Enter age. only positive integer 18—120 ")]
):
	new_id = int(max(users.keys())) + 1 if users else 1
	new_user = {f"{new_id}": f'Имя: {username}, возраст: {age}'}
	users.update(new_user)
	return f"User {new_id} is registered. {new_user}"

@app.put("/user/{user_id}/{username}/{age}")
async def update_task(user_id: str, username: str, age: Annotated[
	int, Path(ge=18, le=120, title='Enter age', description="Enter age. only positive integer 18—120 ")]
):
	for key in users:
		if key == str(user_id):
			new_user={key: f'Имя: {username}, возраст: {age}'}
			users.update(new_user)
			return new_user, f"User {key} has been updated"
	raise HTTPException(status_code=404, detail="Задача не найдена")

@app.delete("/user/{user_id}")
async def delete_task(user_id: str):
	for i, key in enumerate(users):
		if key == user_id:
			del users[key]
			return {"detail": "Задача удалена"},f"User {key} has been deleted"
	raise HTTPException(status_code=404, detail="Задача не найдена")

"""
uvicorn module_16_3:app --reload
"""
