# module_10_1.py
"""
Создание потоков
Задача "Потоковая запись в файлы":
"""
import string
from threading import Thread as t
from requests import get
import requests as r
from datetime import datetime as dt

#PATH='C:\Users\slvl3\AppData\Local\Programs\Python\Python312\Lib\site-packages\requests\requests'

###
def write_words(word_count, file_name):
	try:
		s1= "Какое-то слово №"
		s2= f"Завершилась запись в файл {file_name}"
		with open(file_name,'w',encoding='utf-8') as file:
			from time import sleep
			for n in range(word_count):
				s=f'{s1} {n+1}\n'
				file.write(s)
				sleep(0.01)
			print(s2)
	except BaseException as e:
		print({e.__context__})

params= [\
	(10, 'example1.txt'),\
	(30, 'example2.txt'),\
	[200, 'example3.txt'],\
	[100, 'example4.txt']]

dt1=dt.now()
for p in params:
	print(p)

[write_words(*p) for p in params]

dt2=dt.now()
print(dt2-dt1)

import os
print([f.title() for f in os.listdir() if f.title().lower().endswith('txt')])

t1 = t(target=os.system,args=['d.cmd'])
t1.start()
t1.join()

dt3=dt.now()
try:
	for a in params:
		t1 = t(target=write_words, args=a)
		t1.start()
		t1.join()
except BaseException as e:
	print({e.__repr__()})

dt4=dt.now()
print(dt4-dt3)
#########
URL='https://binaryjazz.us/wp-json/genrenator/v1/genre'
def fn():
	result = []
	args = [URL]

	for i in range(20):
		res = get(URL)
		page=res.json()
		result.append(page)
	print(result)

def get_url():
	t1=t(target=fn)
	t1.start()
	t1.join()

get_url()
