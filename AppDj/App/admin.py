from django.contrib import admin

from App.models import *
#from .models import Client

# Register your models here.

#admin.site.register(Buyer)
#admin.site.register(Game)
admin.site.register(News)
#admin.site.register(Client)

@admin.register(Client)
class BuyerAdmin(admin.ModelAdmin):
	list_display = ('name','id','age',)

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
	list_display = ('name','balance','age',)
	search_fields =  ('name',)
	list_filter = ('balance','age',)
	list_per_page =30

	readonly_fields = ('balance',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ('title','cost','size',)
	search_fields =  ('title',)
	list_filter = ('size','cost',)
	list_per_page = 20
