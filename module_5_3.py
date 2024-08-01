# module_5_3.py
"""
по уроку "Перегрузка операторов."
Задача "Нужно больше этажей":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
"""
# import module_5_1
from module_5_1 import House as Base_class


class Haus:
	def __init__(self, name, floors):
		self.name = name
		self.floors = floors
		Base_class(self.name, floors)

	# Необходимо дополнить класс House следующими специальными методами:
	def __eq__(self, other):
		if isinstance(other, Haus):
			return self.floors == other.floors
		return False

	# - должен возвращать True, если количество этажей одинаковое у self и у other.
	# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и
	# возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении
	# участвует кол-во этажей.
	def __lt__(self, other):
		if isinstance(self, Haus) and isinstance(other, Haus):
			return self.floors < other.floors

	def __le__(self, other):
		if isinstance(self, Haus) and isinstance(other, Haus):
			return self.floors <= other.floors

	def __gt__(self, other):
		if isinstance(self, Haus) and isinstance(other, Haus):
			return self.floors > other.floors

	def __ge__(self, other):
		if isinstance(self, Haus) and isinstance(other, Haus):
			return self.floors >= other.floors

	def __ne__(self, other):
		if isinstance(self, Haus) and isinstance(other, Haus):
			return self.floors != other.floors

	def __add__(self, value):
		self.floors += value
		return self

	# - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
	"""
	#- работают так же как и __add__ (возвращают результат его вызова).
	Остальные методы арифметических операторов, где self - x, other - y:
	"""

	def __radd__(par1, par2):
		if isinstance(par1, Haus):
			par1.__add__(par2)
		elif isinstance(par1, int):
			par1 += par1
		return par1

	def __iadd__(self, value):
		if isinstance(self, Haus):
			self.__add__(value)
		return self

	# __len__(self)  # - должен возвращать кол-во этажей здания self.number_of_floors.
	# __str__(self)	"Название: <название>, кол-во этажей: <этажи>".
	def __len__(self):
		return self.floors

	def __str__(self):
		return f"Название: {self.name}, кол-во этажей: {self.floors}"


###
h1 = Haus('ЖК Эльбрус', 10)
h2 = Haus('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__
h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
print(5 <= 2)
"""
Задача "Нужно больше этажей":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".

Необходимо дополнить класс House следующими специальными методами:
__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
Остальные методы арифметических операторов, где self - x, other - y:
"""
