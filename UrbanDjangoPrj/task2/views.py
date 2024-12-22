from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

def index(request):
	return  render(request,'second_task\\task1.html')

class index2(TemplateView):
	template_name = 'second_task\\task2.html'
