
"""
В модуле user.py создайте модель User, наследованную от ранее написанного Base со следующими атрибутами:
__tablename__ = 'users'
id - целое число, первичный ключ, с индексом.
username - строка.
firstname - строка.
lastname - строка.
age - целое число.
slug - строка, уникальная, с индексом.
tasks - объект связи с таблицей с таблицей Task, где back_populates='user'.
"""

from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import Column,String,Boolean,Integer,Float,ForeignKey

from app.backend.db import Base,engine

class User(Base):

	__tablename__="users"
#	__table_args__={'keep_existing':True}
	__table_args__={'extend_existing': True}

	id=Column(Integer,primary_key=True,index=True)
	username=Column(String)
	firstname=Column(String)
	lastname=Column(String)
	age = Column(Integer)
	slug=Column(String,unique=True,index=True)

	tasks= relationship('Task',back_populates='user')

	class Config:
		from_attributes = True
		orm_mode = True # Указывает, что объект может быть преобразован из ORM (например, SQLAlchemy)

# from sqlalchemy.schema import CreateTable
# print(CreateTable(User.__table__))

#Base.metadata.create_all(bind=engine)
