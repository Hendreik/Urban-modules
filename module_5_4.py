# module_5_4.py
"""
по уроку "Различие атрибутов класса и экземпляра."

Цель: понять разницу между атрибутами объекта и класса, дополнив уже существующий класс.
 Применить метод __new__.

Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно
 удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение
 атрибута houses_history.
"""
# import module_5_3
from module_5_3 import Haus


class Hausen:
	instance = None
	houses_history = ['history:']
	name = ""

	# floors = 0

	def __new__(cls, *args, **kwargs):
		cls.name = args[0]
		# cls.floors = args[1]  # floors
		cls.houses_history.append(cls.name)
		#		cls.__instance = Haus(cls.name, cls.floors)
		return super().__new__(cls)

	def __init__(self, *args):
		self.instance = Haus(self.name, args[1])

	# Необходимо дополнить класс House следующими специальными методами:
	def __del__(self):
		return print(self.houses_history.pop(), " снесён, но он останется в истории")


###
h1 = Hausen('ЖК Эльбрус', 10)
print(id(h1))
print(h1.instance)
print(h1.instance + 1)
print(Hausen.houses_history)
h2 = Hausen('ЖК Акация', 20)
print(Hausen.houses_history)
h3 = Hausen('ЖК Матрёшки', 20)
print(Hausen.houses_history)

# Удаление объектов
del h2
del h3

print(Hausen.houses_history)
"""
"""
