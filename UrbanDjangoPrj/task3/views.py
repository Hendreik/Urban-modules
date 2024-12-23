from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

def index(request):
	title= 'site'
	txt='Игры'
	context={
		'title':title,
		'text':txt,
	}
	return  render(request,'third_task\\index.html',context)

def index1(request):
	title= 'site'
	txt='список '
	context={
		'title':title,
		'text':txt,
	}
	return  render(request,'third_task\\task1.html',context)

class index2(TemplateView):
	template_name = 'third_task\\task2.html'
class index3(TemplateView):
	template_name = 'third_task\\task3.html'
class index4(TemplateView):
	template_name = 'third_task\\task4.html'
