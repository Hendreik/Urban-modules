from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from  .forms import UserRegister
from .models import Buyer,Game

def index(request):
	title= 'site'
	txt='Игры'
	l={'values':['Товары','',''] }
	context={
		'title':title,
		'text':txt,
		'lst': l
	}
	return render(request,'menu.html',context)

def index1(request):
	title= 'site'
	txt='Игры'
	l={'values':['Товары','',''] }

	games=Game.objects.all()
	g=games

	context={
		'title':title,
		'text':txt,
		'lst': g
	}
	return render(request,'task1extend.html',context)

class index2(TemplateView):
	template_name = 'task2extend.html'

class index3(TemplateView):
	template_name = 'index.html'


def index4(request):

	info = {}
	new_user = 0

	if request.method == 'POST':

		users = []
		users= Buyer.objects.all()

		form= UserRegister(request.POST)
		print(form.is_valid(),users)
		if form.is_valid():
			name= form.cleaned_data['username']
			pwd= form.cleaned_data['password']
			rpwd= form.cleaned_data['repeat_password']
			age= form.cleaned_data['age']

			print(name)

			if pwd != rpwd:
				info.update({'error': 'Пароли не совпадают'})
			elif int(age) < 18:
				info.update({'error': 'Вы должны быть старше 18'})
			else:
				for u in users:
					s = str(u)
					if s.__contains__(name):
						info.update({'error': 'такой логин уже есть. Пользователь уже существует'})
					else:
						info.update({'name': 'Приветствуем, '+name})
						new_user=1

	else:
		form = UserRegister()

	info.update({'form': form})
	print(info.values())
	if new_user==1:
		if Buyer.objects.filter(name=name).count() ==0:
			print(0)
			Buyer.objects.create(name=name, balance=0.0, age=18)
		new_user=0

	return render(request,'registration_form.html',info)

