from django.shortcuts import render,redirect
from  django.http import  HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import *

from .forms import *
from .models import *
from django.core.paginator import Paginator
import fastapi
app=fastapi.FastAPI()

# Create your views here.

def django_(request):
	title = 'site'
	txt = 'ORM Django'
	print(txt)
	l = {'values': ['Товары', '', '']}
	context = {
		'title': title,
		'text': txt,
		'lst': l
	}
	return render(request,'dj.html',context)

def alch(request):
	title = 'page'
	txt = 'ORM SQL Alchemy'
	print(txt)
	l = {'values': ['Товары', '', '']}
	context = {
		'title': title,
		'text': txt,
		'lst': l
	}
	return render(request,'dj.html',context)

def tortoise(request):
	title = 'page'
	txt = 'ORM Tortoise'
	print(txt)
	l = {'values': ['Товары', '', '']}
	context = {
		'title': title,
		'text': txt,
		'lst': l
	}
	return render(request,'dj.html',context)

def index1(request):
	title= 'site'
	txt='menu'
	l={'values':['Товары','',''] }
	context={
		'title':title,
		'text':txt,
		'lst': l
	}
	return render(request,'menu.html',context)

def index2(request):
	title= 'site'
	txt='ORM'
	l={'values':['main','',''] }
	context={
		'title':title,
		'text':txt,
		'lst': l
	}
	return render(request,'main.html',context)

def index3(request):
	title= 'site'
	txt='ORM'
	l={'values':['users','',''] }
	context={
		'title':title,
		'text':txt,
		'lst': l
	}
	return render(request,'users.html',context)

#@app.post()
def index4(request):
	if request.method == 'POST':
		name=request.POST.get('uname')
		pwd=request.POST.get('pwd')
		rpwd=request.POST.get('rpwd')
		age=request.POST.get('age_')

		print({name})
		print({pwd})
		print({rpwd})
		print({age})
	title= 'site'
	txt=''
	l={'values':['users','',''] }
	context={
		'title':title,
		'text':txt,
		'lst': l
	}
	return render(request,'users.html',context)

users = ['user1', 'user2']
#
def formUser(request):
	if request.method == 'POST':
		name=request.POST.get('username')
		pwd=request.POST.get('lastname')
		rpwd=request.POST.get('lastname')
		age=request.POST.get('age_')

		print({name})
		print({pwd})
		print({rpwd})
		print({age})

		info = {}
		info.update({'name': {name}})

		return HttpResponse(f"registered {name}")

	return render(request,'forms\\user_form.html',context={'request':request})
########### clients
@app.post("/add")
def htmClient(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		fname = request.POST.get('firstname')
		lname = request.POST.get('lastname_')
		age = request.POST.get('age_')

		print({name})
		print({fname})
		print({lname})
		print({age})

		#info = {}
		info={'name': {name},'firstname': {fname},'lastname': {lname},'age': {age} }
		if name == "":
			print('напишите name ', name)
			info.update({'name': 'напишите name ' + name})

			return HttpResponse(f"registered {name}")
		#info.update({'firstname': {fname}},{'lastname': {lname}},{'age': {age}})
		# print(info.values(),context)
		return render(request, 'forms\\client_form.html',context=info)
#		return render(request,'forms\\client_form.html',context={'request':request})

@app.post("/fc")
def  formClient(request):
	info = {}
	cl=[]
	cl=Client.objects.all()

	if request.method == 'POST':
		form= ClientForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			name= form.cleaned_data['name']
			fname= form.cleaned_data['firstname']
			lname= form.cleaned_data['lastname']
			age= form.cleaned_data['age']
			print(99,name)

			if cl.count() == 0:
				print(0)
				Client.objects.create(name=name, firstname=fname, lastname=lname,age=age)
				return redirect('nsApp:clientsAll')

			else:
				for u in cl:
					s = str(u.name)
					print(4,u.name,len(s),type(s),type(u.name))
					if s.__contains__(name):
						print(4, u.name,name)
						info.update({'error': 'такой name уже есть. Пользователь уже существует'})
					else:
						info.update({'name': 'Приветствуем, '+name})
						print(name)
						Client.objects.create(name=name, firstname=fname, lastname=lname,age=age)
						return redirect('nsApp:clientsAll')
							#render(request, 'ext\\client_ext.html',info))
	else:
		form = ClientForm()

	info.update({'form': form})
	print(info.values())
	return render(request,'forms\\client_form.html',info)

def clients(request):
	cl=Client.objects.all()
	print(cl)
	title= 'site'
	txt='список '
	list_= cl
	context={
		'title':title,
		'text':txt,
		'lst': list_
	}
	return  render(request,'ext\\client_ext.html',context)

@app.post("/fc/del/{id}")
def clientdel(request,id):
	if request.method == 'POST':
	# cl = Client.objects.all()
	# #cl.delete(id=id_)
	# c=cl.get(id=id)
	# post = Client.objects.get(id=id_)
		print(id)
	# post.delete()
	cl = Client.objects.all()

	context = {
		'lst': cl
	}
	return redirect('nsApp:clientsAll')
#render(request,'ext\\client_ext.html',context)
########### messages
def messages(request):
	from datetime import datetime as dt
	msg=News.objects.all()
	print(msg)
	title= 'page News'
	txt='список '
	dt=f'{dt.now().date()}'
	print(dt)
	list_= msg
	context={
		'title':title,
		'text':txt,
		'dt':dt,
		'lst': list_
	}
	return  render(request,'ext\\message_ext.html',context)

		# 	return HttpResponse(f"registered {name}")
		# #info.update({'firstname': {fname}},{'lastname': {lname}},{'age': {age}})
		# # print(info.values(),context)
		# return render(request, 'forms\\client_form.html',context=info)
@app.post("/msg/add")
def htmMsg(request):
	info = {}
	cl=[]
	cl=Client.objects.all()

	if request.method == 'POST':
		form= ClientForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			name= form.cleaned_data['name']
			fname= form.cleaned_data['firstname']
			lname= form.cleaned_data['lastname']
			age= form.cleaned_data['age']
			print(99,name)

			if cl.count() == 0:
				print(0)
				Client.objects.create(name=name, firstname=fname, lastname=lname,age=age)
				return redirect('nsApp:clientsAll')

			else:
				for u in cl:
					s = str(u.name)
					print(4,u.name,len(s),type(s),type(u.name))
					if s.__contains__(name):
						print(4, u.name,name)
						info.update({'error': 'такой name уже есть. Пользователь уже существует'})
					else:
						info.update({'name': 'Приветствуем, '+name})
						print(name)
						Client.objects.create(name=name, firstname=fname, lastname=lname,age=age)
						return redirect('nsApp:clientsAll')
							#render(request, 'ext\\client_ext.html',info))
	else:
		form = ClientForm()

	info.update({'form': form})
	print(info.values())
	return render(request,'forms\\client_form.html',info)

def h(request):
	if request.method == 'POST':
		info = {}
		t = request.POST.get('title')
		cn = request.POST.get('content')
		dt = request.POST.get('date')
		info={'name': {t}}
		if t == "":
			info.update({'name': 'напишите title. Add title ' + t})
			print(info.values())

			return render(request, 'ext\\message_ext.html', context={'info': info})

		print(9, t)
		print({t})
		print({cn})
		print({dt})
		msg = []
		msg = News.objects.all()
		if msg.count() == 0:
			print(0)
			News.objects.create(title=t, content=cn, date=dt)
			return redirect('nsApp:messagesAll')
		else:
			for m in msg:
				s = str(m.title)
				print(t, m.title, len(s), s)
				if s.__eq__(t):
					print(54, m.title, t)
					info.update({'error': 'такой message уже есть. title уже существует'})
					return render(request, 'ext\\message_ext.html', context={'info': info})

			info.update({'name': 'Приветствуем news, ' + t})
			print(t)
			News.objects.create(title=t, content=cn, date=dt)

	return redirect('nsApp:messagesAll')
	# return render(request,'forms\\message_form.html',context={'request':request})

@app.post("/fm/del")	#/<id:int>
def messageDel(request,id_=0):

	info={}
	if request.method == 'POST':
		id_=request.POST.get('id_')
		if id_ == "":
			info.update({'error': 'неправильный id'})
			print(info.get('error'))
			return render(request, 'ext\\message_ext.html', context={'info': info})

		i=(News.objects.filter(id=id_).count())
		if i==0:
			info.update({'errorId': ' / нет такого id в таблице'})
			return render(request, 'ext\\message_ext.html', context={'info': info})

	msg=News.objects.filter(id=id_)
	msg.delete()
	msg=News.objects.all()

	context = {
		'lst': msg
	}
	return redirect('nsApp:messagesAll')

########### users
########### goods
def googs_(request):
	title= 'site'
	txt='Игры'
	l={'values':['Товары','',''] }

	games=Client.objects.all()
	g=games

	context={
		'title':title,
		'text':txt,
		'lst': g
	}
	return render(request,'task1extend.html',context)

