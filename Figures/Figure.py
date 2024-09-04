# Figure.py
"""
 задание по модулю: "Наследование классов."
  классы Figure(родительский), Circle, Triangle и Cube
"""
import math

class Figure:
	"""
	Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
	Атрибуты(публичные): filled(закрашенный, bool)
	"""
	sides_count = 0
	__color = (0, 0, 0)

	def __init__(self, color, sides, filled=False):

		self.__sides = sides
		self.__color = color  # формате RGB
		self.filled = filled

		return 0

	def get_color(self):
		return self.__color

	def __is_valid_color(self, r, g, b):
		# в диапазоне от 0 до 255
		if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
			return True

		return False

	def set_color(self, r, g, b):  # __color
		if self.__is_valid_color(r, g, b):
			self.__color = (r, g, b)
		return 0

	def __is_valid_sides(self, *args):

		if len(self.__sides) == self.sides_count:
			for i in self.__sides:
				if i < 0:
					return False
			return True
		return False

	def get_sides(self):
		return list(self.__sides)

	def __len__(self):
		perimeter = 0
		if isinstance(self, Circle):
			perimeter = self.__sides[0]
		# if isinstance(self, Triangle):
		# perimeter = self.__sides
		# if isinstance(self, Cube):
		# perimeter = self.__sides
		return perimeter

	def set_sides(self, *new_sides):

		if (len(new_sides) == self.sides_count and
				self.__is_valid_sides(new_sides)):
			self.__sides = new_sides
		#		if isinstance(Circle):
		return 0


class Circle(Figure):
	sides_count = 1
	"""
	Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
	Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).	
	"""

	def __init__(self, *args, **filled):

		if isinstance(args[0], tuple):
			color = args[0]

		# sides = []
		n = 1
		match len(args):
			case 2:        n = args[1]
		sides = [n]

		super().__init__(color, sides, filled)
		self.__radius = n / 2 / math.pi

	def get_square(self):
		print("площадь круга", end=" ")
		return math.sqrt(self.__radius) * math.pi


class Triangle(Figure):
	sides_count = 3

	"""
	Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
	"""

	def __init__(self, *args, **filled):

		if isinstance(args[0], tuple):
			color = args[0]

		sides = []
		n = 1
		match len(args):
			case 4:  #
				sides.append(args[1])
				sides.append(args[2])
				sides.append(args[3])
			case _:
				while len(sides) < self.sides_count:
					sides.append(n)

		super().__init__(color, sides, filled)

	def get_square(self):
		print("площадь треугольника", end=" ")  # по формуле Герона
		sides = self.get_sides()
		print(sides)
		a = sides[0]
		b = sides[1]
		c = sides[2]
		# равнобедренного
		if a == b or a == c or b == c:
			if b > a:
				a = b
				b = c
			if c > a: a = c
			n1 = b / 2
			n2 = math.sqrt(math.fabs(a * a - (c * c) / 4))
			s = n1 * n2

		# произвольного
		else:
			a = a * a
			b = b * b
			c = c * c
			n1 = math.pow(a + b + c, 2)
			n2 = 2 * (a * a + b * b + c * c)
			s = math.sqrt(math.fabs(n1 - n2)) / 4

		return '{:.4}'.format(s)


class Cube(Figure):
	sides_count = 12
	"""
	Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
	Метод get_volume, возвращает объём куба
	"""

	def __init__(self, *args, **filled):

		if isinstance(args[0], tuple):
			color = args[0]

		sides = []
		n = 1
		match len(args):
			case 2:     n = args[1]

		while len(sides) < self.sides_count:
			sides.append(n)

		super().__init__(color, sides, filled)

	def get_volume(self):
		print("Oбъём куба", end=" ")
		n = self.get_sides()
		side = n[0]
		return math.pow(side, 3)
