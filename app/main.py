# Структура проекта. Маршруты и модели Pydantic.
"""
Задача "Основные маршруты":
Необходимо создать маршруты и написать Pydantic модели для дальнейшей работы.
В файле main.py создайте сущность FastAPI(), напишите один маршрут для неё - '/', по которому функция возвращает
 словарь - {"message": "Welcome to Taskmanager"}.
Импортируйте объекты APIRouter и подключите к ранее созданному приложению FastAPI, объединив все маршруты в одно
 приложение.

# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from models import User
from schemas import * #CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

"""
#from app import *

# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from models.user import User
import models as m
from schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

import backend.db as db
import schemas as sc
import routers.user as r_user
import routers.task as r_task
#import routers.category as rc
from routers import task,user

from fastapi import FastAPI
from fastapi import APIRouter, Depends, status, HTTPException

router= APIRouter()
ap = FastAPI()

@ap.get("/")
async def main():
	return {"message": "Welcome to Taskmanager"}

#ap.include_router(r_user.router)
ap.include_router(task.router)
# app.include_router(rc)

@ap.get("/main")
async def main():
	return {"main":"Shop"}

@ap.get("/all")
async def get_all(db: Annotated[Session,Depends(get_db)]):
	categories= db.scalar(select(User).where(User.id > 0)).all()
	return categories

router_u= APIRouter(prefix="/user",tags=["user"])
	#r_user.router)
ap.include_router(router_u)

@router_u.post("/create")
async def create_user():
# 		db: Annotated[Session,Depends(get_db)],create_user:sc.CreateUser):
# 	db.execute(insert(user).values(name=create_user.name,
# parent_id=create_user.parent_id,
# slug=slugify(create_user.name)))
# 	db.commit()
	return {'status_code': status.HTTP_201_CREATED,
			'transaction': 'Successful'}

if __name__=="__main__":
#	import uvicorn

#	import app.backend.db as db
	print(__name__)
	db.Base.metadata.create_all(bind=db.engine)

"""
cd module17db

cd app
uvicorn main:app --reload
"""
"""
alembic revision --autogenerate -m "init migration"

alembic upgrade head
"""













































