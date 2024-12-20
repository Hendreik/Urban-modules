"""
 схемы в модуле schemas.py, наследуемые от BaseModel, для удобной работы с будущими объектами БД:
CreateUser с атрибутами: username(str), firstname(str), lastname(str) и age(int)
UpdateUser с атрибутами: firstname(str), lastname(str) и age(int)
CreateTask с атрибутами: title(str), content(str), priority(int)
UpdateTask с теми же атрибутами, что и CreateTask.
"""
from pydantic import BaseModel

class CreateUser(BaseModel):
	username:str
	firstname: str
	lastname: str
	age: int
	# name: str
	# description:str
	# price: float
	# image_url:str
	# stock: int
	# category: int

class UpdateUser(BaseModel):
	firstname: str
	lastname: str
	age: int

class CreateTask(BaseModel):
	title: str
	content: str
	priority: int


class UpdateTask(BaseModel):
	title: str
	content: str
	priority: int












