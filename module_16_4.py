# module_16_4.py
"""
Модели данных Pydantic

"""
from pydantic import BaseModel, Field
from typing import List,Annotated
from fastapi import FastAPI, HTTPException,Path

class  User(BaseModel):
	id: int
	username: str=Field(...,description="")
	age: int=Field(...,description="Enter age. only positive integer 18—120 ")

users: List[User] = [
#	User(id=1,username="u1",age=22)
]

app=FastAPI()
@app.get("/")
async def read_root() -> dict:
	return {"root": "Главная страница"}


@app.get("/users", response_model=List[User])
async def get_tasks():
	return users

@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str,age: Annotated[
	int, Path(ge=18, le=120, title='Enter age', description="Enter age. only positive integer 18—120 ")]
):
	new_id = max((t.id for t in users), default=0) + 1
	new_user = User(id=new_id, username=username, age= age)
	users.append(new_user)
	return new_user


#Обновление существующей задачи (PUT)
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_task(user: User):
	for u in users:
		if u.id == user.id:
			new_user = User(id=user.id,username=user.username,age=int(user.age))
			users.remove(u)
			users.append(new_user)
			return new_user
	raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_task(user_id: int):
	for u in users:
		if u.id == user_id:
			users.remove(u)
			return {"detail": "Задача удалена"},f"User < {u} > has been deleted"
	raise HTTPException(status_code=404, detail="User was not found")

"""
uvicorn module_16_4:app --reload
"""
