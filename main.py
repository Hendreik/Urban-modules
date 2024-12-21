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
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models.user import User
import app.models as m
from app.schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify
import unicodedata

import app.backend.db as db
import app.schemas as sc
import app.routers.user as r_user
import app.routers.task as r_task
#import routers.category as rc
from app.routers import task,user

from fastapi import FastAPI
from fastapi import APIRouter, Depends, status, HTTPException

router= APIRouter()
#app = FastAPI(prefix='Application',title='Root',description='/'+db.DBS_)
app = FastAPI(prefix='Application',title='Root',description='/'+db.get_name(),
swagger_ui_parameters={"tryItOutEnabled": True,"reload":True}, debug=True)

@app.get("/")
async def main():
	return {"message": "Welcome to Taskmanager"}

app.include_router(r_user.router)
app.include_router(task.router)

@app.get("/main")
async def main_():
	return {"main":"Root"}

@app.get("/all", response_model=None)
def read_(db: Session = Depends(get_db)):
#def read_(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
	#stmt = select(User).offset(skip).limit(limit)
	stmt = select(User)
	print(stmt)
	result = db.scalars(statement=stmt).all()
	r=db.scalars(statement=stmt).first().slug
	if result: print('slug[id=1]  ',result.__getitem__(0).slug,r)
	return result


@app.get("/all*", response_model=None)
def get_all(db: Annotated[Session,Depends(get_db)]):
	res= db.scalars(select(User).where(User.id > 0)).fetchall()
	return res

if __name__=='__main__':
	import uvicorn
	uvicorn.run(app, host="localhost", port=8000)

"""
Создайте 3 записи User с соответствующими параметрами:
username: user1, user2, user3
firstname: Pasha, Roza, Alex
lastname: Technique, Syabitova, Unknown
age: 40, 62, 25
Измените запись с id=3: firstname = Bear, lastname = Grylls, age = 50
Удалите запись с id =2.
Выведите всех пользователей.

cd module17db\\app

uvicorn main:app --reload
"""
"""
alembic revision --autogenerate -m "init migration"

alembic upgrade head
"""













































