"""
URL configuration for AppDj project.

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
from django.conf import settings

# \app\models
_DBS_= settings.DBS_		#"sqlite:///../../data.db"
# \root
#_DBS_="sqlite:///../../.db"
print(_DBS_)

from django.contrib import admin
from django.urls import path, include
from  django.views.generic import TemplateView
from django.views.generic import RedirectView

from App.views import *
import App.views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', TemplateView.as_view(template_name='start.html')),

	path('', include('App.urls')),
	path('dj/',include('App.urls')),
	# path('Alchemy/',include('App.urls')),
	# path('Tortoise/',include('App.urls')),
]
	# path('users/',App.views.index1),
#	path('', RedirectView.as_view(url='/', permanent=True)),
	# path('app/', include('App.urls'),name="App"),
	# path('messages/', TemplateView.as_view(template_name='users.html')),
	# path('dashboard/', App.views.index2, name='dashboard'),
	# path('1/', App.views.index2, name='1'),
	# path('2/', index2, name='2'),
	# path('home/',index4,name='home_'),
		 # ext/
	# path('1/', TemplateView.as_view(template_name='ext/base.html')),
	# #path('2/', TemplateView.as_view(template_name='ext/1base.html')),
	# path('home/', TemplateView.as_view(template_name='ext/home.html')),
	# path('4/', TemplateView.as_view(template_name='ext/login.html')),
	# path('5/', TemplateView.as_view(template_name='ext/register.html')),
	# path('6/', TemplateView.as_view(template_name='ext/dashboard.html')),
	# path('7/', TemplateView.as_view(template_name='ext/add_image.html')),
	# path('8/', TemplateView.as_view(template_name='ext/add_video.html')),

#    path('image/delete/<int:image_id>/', delete_image, name='delete_image'),
#]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)