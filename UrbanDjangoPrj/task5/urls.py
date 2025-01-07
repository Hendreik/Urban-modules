
from django.contrib import admin
from django.urls import path
from  django.views.generic import TemplateView

from .views import sign_up_by_html, sign_up_by_django as f51

urlpatterns = [
	path('1/', sign_up_by_html, name='html'),
	path('', f51, name='h'),

]