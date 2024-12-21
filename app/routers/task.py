"""
Маршруты:
В модуле task.py напишите APIRouter с префиксом '/task' и тегом 'task', а также следующие маршруты, с пустыми функциями:
get '/' с функцией all_tasks.
get '/task_id' с функцией task_by_id.
post '/create' с функцией create_task.
put '/update' с функцией update_task.
delete '/delete' с функцией delete_task.
"""
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

from app.models import Task
from app.schema.tasks import *

from fastapi import APIRouter, Depends, status, HTTPException

router= APIRouter(prefix="/task",tags=["task"])

@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
	ret_ = db.query(Task)
	print(ret_)
	if ret_:
		return ret_.all(), {'status_code': status.HTTP_200_OK}

	raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)

@router.get("/task_id")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
	ret_ = db.query(Task).filter(Task.id == int(task_id)).first()
	print(ret_)
	if ret_ is None:
		raise HTTPException(status_code=404, detail=" not found")
	return ret_, {'status_code': status.HTTP_200_OK}

#@router.post("/create", response_model=None)
# async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):

# 		db.commit()
# 		stmt = select(User)
# 		tbl = db.scalar(stmt)
# 		if tbl is None:
# 			raise HTTPException(status_code=404, detail=" not found")
# 		db.refresh(tbl)
# 		return create_user.username, _ok_

_ok_ = {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask,user_id: int):
	print( create_task)
	with db:
		ret=db.execute(insert(Task).values(title=create_task.title,
content=create_task.content,
user_id =user_id,
))
		db.commit()
		stmt = select(Task)
		tbl = db.scalar(stmt)

		if tbl is None:
			raise HTTPException(status_code=404, detail=" not found")
		db.refresh(tbl)
		return create_task.title, _ok_

#	title: str
	# content: str
	# priority: int
	# completed: bool
	# slug: str
	# user_id: str

@router.put("/update")
async def update_task(task_id: int,db: Annotated[Session, Depends(get_db)], update_task:UpdateTask):
	print( {"update ...":f"update_ {task_id}"})
	stmt = select(Task).where(Task.id == task_id)
	ret = db.scalars(stmt)
	if ret.first() is None:
		print({'status_code=404': f"id {task_id} not found"})
		raise HTTPException(status_code=424, detail={'status_code': status.HTTP_424_FAILED_DEPENDENCY, 'transaction': f'id= {task_id} update impossible!'})

	with db:
		ret=db.execute(update(Task).values(title=update_task.title,
content=update_task.content,
priority =update_task.priority,
completed=update_task.completed,
slug=update_task.slug
#user_id=update_task.user_id
).where(Task.id==task_id))

		db.commit()
		return update_task.title, {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete("/delete")
async def delete_task(user_id: int,db: Annotated[Session, Depends(get_db)]):
	res ={"to delete ...": f" user_id {user_id}"}
	print(res)
	try:
		with db:
			u = db.scalar(select(Task).where(Task.id == user_id))
			if u is None:
				raise HTTPException(status_code=404, detail=" not found")

			db.execute(delete(Task).where(Task.id == user_id))
			db.commit()
			return res
	except Exception as e:
			raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)


