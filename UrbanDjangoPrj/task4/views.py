from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

def index(request):
	title= 'site'
	txt='Игры'
	l={'values':['Atomic',2.2,3] }
	context={
		'title':title,
		'text':txt,
		'lst': l
	}
	return render(request,'fourth_task\\menu.html',context)

def base(request):
	return render(request,'fourth_task\\extend.html')

def index1(request):
	title= 'site'
	txt='список '
	context={
		'title':title,
		'text':txt,
	}
	return  render(request,'fourth_task\\task1extend.html',context)

class index2(TemplateView):
	template_name = 'fourth_task\\task2extend.html'

def index3(request):
	name= 'it is 3'
	txt='список '
	l=['asdf1',2.2,3]
	context={
		'title':name,
		'text':txt,
		'lst':l
	}
	return  render(request,'fourth_task\\task3.html',context)

def index4(request):
	name= 'it is 4'
	txt='список '
	l={'values':['Atomic',2.2,3] }
	context={
		'title':name,
		'text':txt,
		'lst':l
	}
	return  render(request,'fourth_task\\task4.html',context)

# class index4(TemplateView):
# 	template_name = 'fourth_task\\task4.html'
