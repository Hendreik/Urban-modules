# module_9_5.py
"""
"Итераторы"
-5 -4 -3 -2 -1 0 1
6 8 10 12 14
5 4 3 2 1
"""


class StepValueError(ValueError):
	pass


class Iterator:
	def __init__(self, start, stop, step=1):
		s_e = 'шаг не может быть равен 0'
		if step == 0:
			print(s_e)
			raise StepValueError(s_e)
		self.start = start
		self.stop = stop
		self.step = step
		self.pointer = start

	def __iter__(self):
		self.pointer = self.start
		return self

	def __next__(self):
		if self.pointer == self.start:
			ret = self.start
		else:
			ret = None

		self.pointer += self.step
		"""
		__next__ - метод увеличивающий атрибут pointer на step. В зависимости от знака атрибута step итерация
		 завершиться либо когда pointer станет больше stop, либо меньше stop. Учтите это при описании метода.
		"""
		if (self.step < 0 and self.stop > self.pointer) or (self.step > 0 and self.stop < self.pointer):
			raise StopIteration()

		if ret == self.start:
			return f'{ret} {self.pointer}'

		return self.pointer


try:
	iter1 = Iterator(100, 200, 0)
	for i in iter1:
		print(i, end=' ')
except StepValueError:
	print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
	print(i, end=' ')
print()
for i in iter3:
	print(i, end=' ')
print()
for i in iter4:
	print(i, end=' ')
print()
for i in iter5:
	print(i, end=' ')
print()
