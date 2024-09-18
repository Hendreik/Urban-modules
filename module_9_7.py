# module_9_7.py
"""
Декораторы
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
 "Составное" в противном случае.
Примечания:
Не забудьте написать внутреннюю функцию wrapper в is_prime
Функция is_prime должна возвращать wrapper
@is_prime - декоратор для функции sum_three
"""


def sum_three(*args):
	print(sum(args))


sum_three(1, 2, 3)


def is_prime(function):
	def wrapper(*args):
		return function(*args)

	return wrapper


@is_prime
def sum_three(*args):
	return sum(args)


print(sum_three(-1, 2, 3))

result = sum_three(2, 3, 6)
print(result)
