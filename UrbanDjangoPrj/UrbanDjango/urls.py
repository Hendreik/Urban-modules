"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  django.views.generic import TemplateView

from task2.views import index, index2
from task3.views import index as i, index1 as i1, index2 as i2, index3 as i3

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', i),
	path('1/', i1),
	path('2/', TemplateView.as_view(template_name='third_task\\task2.html')),
	path('3/', TemplateView.as_view(template_name='third_task\\task3.html')),
	path('t2', index),
	path('t2/1', index2),
]












