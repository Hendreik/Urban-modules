"""
# Структура проекта. Маршруты и модели Pydantic.

В модуле user.py напишите APIRouter с префиксом '/user' и тегом 'user', а также следующие маршруты, с пустыми функциями:
get '/' с функцией all_users.
get '/user_id' с функцией user_by_id.
post '/create' с функцией create_user.
put '/update' с функцией update_user.
delete '/delete' с функцией delete_user.

from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from models import User
from schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify
"""
from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД

import app.backend.db as db

from app.backend.db_depends import get_db
# # Аннотации, Модели БД и Pydantic.
from typing import Annotated, List
# from models import User
from app.schemas import CreateUser, UpdateUser
from app.models.user import User
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/users", response_model=None)
async def all_users(db: Annotated[Session, Depends(get_db)]):
	user_ = db.query(User)
	return user_.all(), {'status_code': status.HTTP_200_OK}


@router.get('/user_id')
async def _user(user_id: int, db: Annotated[Session, Depends(get_db)]):
	user_ = db.query(User).filter(User.id == int(user_id)).first()
	print(user_)
	if user_ is None:
		raise HTTPException(status_code=404, detail=" not found")
	return user_, {'status_code': status.HTTP_200_OK}


@router.get('{/user_id}')
async def _userScalar(user_id: int, db: Annotated[Session, Depends(get_db)]):
	print(user_id)
	stmt = select(User).where(User.id == user_id)
	sess = db.scalar(stmt)
	if sess is None:
		raise HTTPException(status_code=404, detail=" not found")
	return sess


_ok_ = {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.post("/user_id")
def create_(cru: CreateUser, session: Session = Depends(get_db)):
	db_ok = User(username=cru.username, firstname=cru.firstname, lastname=cru.lastname, age=cru.age, slug=cru.slug)
	session.add(db_ok)
	session.commit()
	session.refresh(db_ok)
	return db_ok, _ok_


@router.post("/create", response_model=None)
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
	with db:
		db.execute(insert(User).values(username=create_user.username,
									   firstname=create_user.firstname, lastname=create_user.lastname,
									   age=create_user.age,
									   slug=create_user.slug))
		db.commit()
		stmt = select(User)
		tbl = db.scalar(stmt)
		if tbl is None:
			raise HTTPException(status_code=404, detail=" not found")
		db.refresh(tbl)
		return create_user.username, _ok_


# except Exception as e:
# 	print("error",e.__class__)


@router.put("/update")
async def update_user(user_id: int,db: Annotated[Session, Depends(get_db)], update_user: UpdateUser):
	print( {"update ...":f"update_user {user_id}"})
	with db:
		db.execute(update(User).values(username=update_user.username,
firstname=update_user.firstname, lastname=update_user.lastname,
age=update_user.age
).where(User.id==user_id))
#slug=update_user.slug))
		db.commit()
		stmt = select(User)
		tbl = db.scalar(stmt)
		if tbl is None:
			raise HTTPException(status_code=404, detail=" not found")
		db.refresh(tbl)
		return update_user.username, {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete("/delete")
async def delete_user(user_id: int,db: Annotated[Session, Depends(get_db)]):
	res ={"delete ...": f"deleted user_id {user_id}"}
	print(res)
	try:
		with db:
			u = db.scalar(select(User).where(User.id == user_id))
			if u is None:
				raise HTTPException(status_code=404, detail=" not found")

			db.execute(delete(User).where(User.id == user_id))
			db.commit()
			return res
	except Exception as e:
			raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)

#DELETE FROM users
# user = session.scalar(select(User).where(User.id == 1))
# return user.tasks
# session.query()
# session.get()
# session.get_one()
