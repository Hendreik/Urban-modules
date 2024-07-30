# module_5_2.py
"""
по уроку "Специальные методы классов"
Необходимо дополнить класс House следующими специальными методами:
"""
# import module_5_1
from module_5_1 import House as base_class


class haus:
	def __init__(self, name, floors):
		self.name = name
		self.floors = floors
		base_class(self.name, floors)

	# __len__(self)  # - должен возвращать кол-во этажей здания self.number_of_floors.
	# __str__(self)	"Название: <название>, кол-во этажей: <этажи>".
	def __len__(self):
		return self.floors

	def __str__(self):
		return f"Название: {self.name}, кол-во этажей: {self.floors}"


###
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#	base_class('ЖК Эльбрус', 30)
h1 = haus('ЖК Эльбрус', 10)
h2 = haus('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
#
