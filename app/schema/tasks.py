"""
 схемы в модуле schemas.py, наследуемые от BaseModel, для удобной работы с будущими объектами БД:
CreateUser с атрибутами: username(str), firstname(str), lastname(str) и age(int)
UpdateUser с атрибутами: firstname(str), lastname(str) и age(int)
CreateTask
UpdateTask
"""
from pydantic import BaseModel

class CreateUser(BaseModel):
	username:str
	firstname:str
	lastname:str
	age: int
	slug: str

class UpdateUser(BaseModel):
	username:str
	firstname: str
	lastname: str
	age: int

class CreateTask(BaseModel):
#	id: int
	title: str ="  "
	content: str ="   "
	priority: int =0
	completed: bool = False
	slug: str = "   "
#	user_id:


class UpdateTask(BaseModel):
#	id: int
	title: str= "  "
	content: str="  "
	priority: int=0
	completed: bool=True
	slug: str =" "
#	user_id: int












