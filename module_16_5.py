# module_16_5.py
"""
научиться взаимодействовать с шаблонами Jinja 2 и использовать их в запросах.

Задача "Список пользователей в шаблоне":
"""
from fastapi import FastAPI, Request, HTTPException, Path, Form  # pip install python-multipart
from fastapi import status, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates
from typing import Annotated, List

# app = FastAPI()
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True, "reload": True}, debug=True)

templates = Jinja2Templates(directory="templates")

users_db = []
# username - UrbanUser, age - 24
# username - UrbanTest, age - 22
# username - Capybara, age - 60

class User(BaseModel):
	id: int
	username: str = Field(..., description="username")
	age: int

users: List[User] = [
	User(id=0, username="UrbanUser", age=24),
	User(id=1, username="UrbanTest", age=22),
	User(id=2, username="Capybara", age=60)
]
print(users)

class Users(BaseModel):
	id: int = None
	text: str
	age: int = Field(..., description="Enter age. only positive integer 18—120 ")


users_db.append(Users(id=0, text='0-message', age=55))
print(users_db)

###########
messages_db = []


class Message(BaseModel):
	id: int = None
	text: str


@app.get("/")
async def get_all_(request: Request) -> HTMLResponse:
	return templates.TemplateResponse("start.html", {"request": request, "messages": None})


################

@app.get("/users")
async def get_all_(request: Request) -> HTMLResponse:
	return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/messages")
async def get_all_messages(request: Request) -> HTMLResponse:
	return templates.TemplateResponse("messages.html", {"request": request, "messages": messages_db})


@app.get(path="/message/{message_id}")
def get_message(request: Request, message_id: int) -> HTMLResponse:
	try:
		return templates.TemplateResponse("messages.html", {"request": request, "message": messages_db[message_id]})
	except IndexError:
		raise HTTPException(status_code=404, detail="Message not found")


@app.get(path="/user/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
	try:
		return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id],
														 "text": users[user_id].username})
	except IndexError:
		raise HTTPException(status_code=404, detail="User not found")


#############
@app.post("/", status_code=status.HTTP_201_CREATED)
def create_message(request: Request, message: str = Form()) -> HTMLResponse:
	if messages_db:
		message__id = max(messages_db, key=lambda m: m.id).id + 1
	else:
		message__id = 0
	messages_db.append(Message(id=message__id, text=message))
	return templates.TemplateResponse("messages.html", {"request": request, "message": messages_db[message__id]})


@app.post("/message",status_code=status.HTTP_201_CREATED)
def add_message(request: Request, message: str = Form()) -> HTMLResponse:
	message__id = len(messages_db)
	messages_db.append(Message(id=message__id, text=message))
	return templates.TemplateResponse("messages.html", {"request": request, "message": messages_db[message__id]})


####################
@app.post("/u", status_code=status.HTTP_201_CREATED)
def create_(request: Request, message: str = Form()) -> HTMLResponse:
	if users_db:
		message__id = max(users_db, key=lambda m: m.id).id  # + 1
	else:
		message__id = 0
	users_db.append(Users(id=message__id, text=message, age=50))
	return templates.TemplateResponse("users.html", {"request": request, "user": users_db[message__id]})

@app.post("/user")
def create_message(request: Request, age: int = Form(), message: str = Form()) -> HTMLResponse:
	__id = len(users)
	users.append(User(id=__id, username=message, age=age.__int__()))
	return templates.TemplateResponse("users.html", {"request": request, "user": users[__id],"text": users[__id].username})

@app.put("/user/{User}")
async def update_task(user: User):
	for u in users:
		if u.id == user.id:
			new_user = User(id=user.id,username=user.username,age=user.age.__int__())
			users.remove(u)
			users.append(new_user)
			return new_user
	raise HTTPException(status_code=404, detail="User was not found")
#######################
@app.delete("/user/{user_id}")
def delete_user(request: Request, user_id: int) -> str:
	try:
		users.pop(user_id)
		return f"User ID={user_id} deleted!"

	except IndexError:
		raise HTTPException(status_code=404, detail="User not found")
#------------------------------
if __name__ == "__main__":
	import uvicorn
	from uvicorn import run

"""
	 uvicorn module_16_5:app --reload
"""
