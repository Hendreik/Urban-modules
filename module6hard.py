# module6hard.py
"""
 задание по модулю: "Наследование классов."
  классы Figure(родительский), Circle, Triangle и Cube
"""


class Figure:
	sides_count = 0
	__color = (0, 0, 0)


"""

"""


def __init__(self, sides, color, filled):
	self.__sides = sides
	self.__color = color
	self.filled = filled


# формате RGB

def get_color(self):
	pass


def __is_valid_color(self, r, g, b):
	# в диапазоне от 0 до 255
	return 0


def set_color(self, r, g, b):
	# __color
	return 0


def __is_valid_sides(self, *args):
	return 0


def get_sides(self):
	return self.__sides


def __len__(self):
	perimeter = 0
	return perimeter


def set_sides(self, *new_sides):
	# sides_count
	return 0


class Circle(Figure):
	sides_count = 1


"""
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).	
"""


class Triangle(Figure):
	sides_count = 3


"""
Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
"""


class Cube(Figure):
	sides_count = 12


"""
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба
"""
