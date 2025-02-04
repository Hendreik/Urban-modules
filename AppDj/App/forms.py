from django import forms

class ClientForm(forms.Form):
	name = forms.CharField(max_length=30, label='Введите name', required=True)
	firstname = forms.CharField(min_length=1, label='Введите firstname')
	lastname = forms.CharField(min_length=0, label='lastname')
	age = forms.CharField(max_length=2, label='Введите свой возраст')

class UserForm(forms.Form):
	username = forms.CharField(max_length=30, label='', required=True)
	firstname = forms.CharField(min_length=1, label='Введите firstname')
	lastname = forms.CharField(min_length=0, label='lastname ')
	age = forms.CharField(max_length=3, label='Введите свой возраст')
	slug = forms.CharField(min_length=8, label='slug')
