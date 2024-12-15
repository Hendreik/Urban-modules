"""
# Структура проекта. Маршруты и модели Pydantic.

В модуле user.py напишите APIRouter с префиксом '/user' и тегом 'user', а также следующие маршруты, с пустыми функциями:
get '/' с функцией all_users.
get '/user_id' с функцией user_by_id.
post '/create' с функцией create_user.
put '/update' с функцией update_user.
delete '/delete' с функцией delete_user.
"""
from fastapi import APIRouter

router= APIRouter(prefix="/user",tags=["user"])

@router.get("/")
async def all_users() -> dict:
	return {"main":"all_users"}


@router.get("/user_id")
async def user_by_id() -> dict:
	return {"main":"user_id"}

@router.post("/create")
async def create_user() -> dict:
	return {"main":"create_user"}

@router.put("/update")
async def update_user() -> dict:
	return {"main":"update_user"}

@router.delete("/delete")
async def delete_user() -> dict:
	return {"main":"delete_user"}



