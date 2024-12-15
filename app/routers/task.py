"""
Маршруты:
В модуле task.py напишите APIRouter с префиксом '/task' и тегом 'task', а также следующие маршруты, с пустыми функциями:
get '/' с функцией all_tasks.
get '/task_id' с функцией task_by_id.
post '/create' с функцией create_task.
put '/update' с функцией update_task.
delete '/delete' с функцией delete_task.
"""
from fastapi import APIRouter

router= APIRouter(prefix="/task",tags=["task"])

@router.get("/")
async def all_tasks() -> dict:
	return {"main":"True"}


@router.get("/task_id")
async def task_by_id() -> dict:
	return {"main":"task_by_id"}

@router.post("/create")
async def create_task() -> dict:
	return {"main":"create_task"}

@router.put("/update")
async def update_task() -> dict:
	return {"main":"update_task"}

@router.delete("/delete")
async def delete_task() -> dict:
	return {"main":"delete_task"}

