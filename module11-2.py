# module11-2.py
"""
1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
"""

import inspect as in_
from pprint import pprint

class Klass:
	def __init__(self):
		self.num=101
		self.st1='string'
		self.list1={self.num:self.st1}
		self.list2=[self.num,self.st1]

	def metod_(self):
		return

def  introspection_info(obj):
	pprint(type(obj))
	pprint(in_.getmodule(obj))
	print('*'* 10)
	for atr in dir(obj):
		pprint(getattr(obj,atr))
	print('='* 10)
	return


obj1 = Klass()
obj2 = obj1.num
obj3 = obj1.st1
obj4 = obj1.list1
obj5 = obj1.list2

introspection_info(obj1)
introspection_info(obj2)
introspection_info(obj3)
introspection_info(obj4)
introspection_info(obj5)