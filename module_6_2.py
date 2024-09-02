# module_6_2.py
"""
Доступ к свойствам родителя. Переопределение свойств.
Цели: Применить сокрытие атрибутов и повторить наследование.
создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) - наследник класса Vehicle.

I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
Атрибут owner(str) - владелец транспорта. (владелец может меняться)
Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
А так же атрибут класса:
Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)
Каждый объект Vehicle должен содержать следующий методы:
Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color; а так же
 владельца в конце в формате "Владелец: <имя>"
Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color,
"""


class Vehicle:
	__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

	def __init__(self, *args):
		self.owner = args[0]
		self.__model = args[1]
		self.__engine_power = args[3]
		self.__color = args[2]

	def get_model(self):
		print("Модель:", self.__model)

	def get_horsepower(self):
		print("Мощность двигателя:", self.__engine_power)
		return 0

	def get_color(self):
		print("Цвет:", self.__color)
		return 0

	def print_info(self):
		self.get_model()
		self.get_horsepower()
		self.get_color()
		print("Владелец:", self.owner)

	def set_color(self, new_color):
		for n in self.__COLOR_VARIANTS:
			if n.upper() == new_color.upper():
				self.__color = new_color
				return 0
		print("Нельзя сменить цвет на", new_color)
		return -1


# Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
# Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)
class Sedan(Vehicle):
	__PASSENGERS_LIMIT = 5

	def __init__(self, *args):
		self.args = args
		super().__init__(*args)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
