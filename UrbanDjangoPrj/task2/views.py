from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

def index(request):
	title= 'site'
	txt='texture'
	context={
		'title':title,
		'text':txt,
	}
	return  render(request,'second_task\\task1.html',context)
def index2(request):
	title= 'site'
	txt='texture'
	context={
		'title':title,
		'text':txt,
	}
	return  render(request,'second_task\\task2.html',context)
