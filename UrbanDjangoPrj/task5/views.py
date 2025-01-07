from django.shortcuts import render
from  django.http import  HttpResponse
from  .forms import UserRegister

# Create your views here.
users = ['user1', 'user2']
def sign_up_by_html(request):
	if request.method == 'POST':
		name=request.POST.get('uname')
		pwd=request.POST.get('pwd')
		rpwd=request.POST.get('rpwd')
		age=request.POST.get('age_')

		print({name})
		print({pwd})
		print({rpwd})
		print({age})

		info = {}
		info.update({'name': {name}})

		return HttpResponse(f"registered {name}")

	return render(request,'fifth_task\\registration_page.html',context={'request':request})

def sign_up_by_django (request):
	info = {}

	if request.method == 'POST':
		form= UserRegister(request.POST)
		print(form.is_valid())
		if form.is_valid():
			name= form.cleaned_data['username']
			pwd= form.cleaned_data['password']
			rpwd= form.cleaned_data['repeat_password']
			age= form.cleaned_data['age']

			print(name)

			if pwd != rpwd:
				info.update({'error': 'Пароли не совпадают'})
			elif int(age) < 18:
				info.update({'error': 'Вы должны быть старше 18'})
			else:
				for u in users:
					if u == name:
						info.update({'error': 'такой логин уже есть. Пользователь уже существует'})
					else:
						info.update({'name': 'Приветствуем, '+name})

	else:
		form = UserRegister()

	info.update({'form': form})
	print(info.values())
	return render(request,'fifth_task\\registration_form.html',info)




