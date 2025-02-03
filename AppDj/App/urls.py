from django.contrib import admin
from django.urls import path, include
from  django.views.generic import TemplateView,RedirectView
from .views import *

app_name = 'nsApp'

urlpatterns = [

	path('', django_, name='django'),

	path('dj/', django_, name='django'),
	path('Alchemy/', alch),
	path('Tortoise/', tortoise),

	path('fc/', formClient, name='clients'),
	path('add/', formClient, name='clients'),
	#	path('fc/<int:frm>/', formClient, name='clients'),
 	path('fc/del/', clientdel, name='clientDel'),
	path('fc/del/{id}/', clientdel, name='delete_cl'),
	path('clients/', clients, name='clientsAll'),
	path('dj/clients/', clients, name='clientsAll'),

	path('msg/add/', htmMsg, name='msg'),
	path('fm/del/', messageDel, name='delete_msg'),
	path('fm/del/<int:id_>/', messageDel, name='delete_msg'),
	#path('messages/', TemplateView.as_view(template_name='ext\\message_ext.html')),
	path('messages/', messages, name='messagesAll'),
]
# 	#	path('messages/', TemplateView.as_view(template_name='users.html')),
#
# 	path('1/', index1, name='1'),
# 	path('fu/', formUser, name='users'),
# 	path('dashboard/', index2, name='dashboard'),
# 	path('2/', index2, name='2'),
# 	path('home/', index2, name='home'),
# 	path('users/', formUser, name='clients'),
# 	path('user/{id}', index4, name='u'),
# ]
