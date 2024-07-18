# module3hard.py
# Дополнительное практическое задание по модулю: "Подробнее о функциях."
data_structure = [
	#  [1, 2, 3,'e'],
	[1, 2, 3],
	{'a': 4, 'b': 5},
	(6, {'cube': 7, 'drum': 8}),
	"Hello",
	((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum_all = 0


def f_calc(i):
	global sum_all
	#	print(sum_all)
	if isinstance(i, list):
		for l in i:
			sum_ = 0
			if type(l) == int:
				sum_ = (l)
			elif type(l) == str:
				sum_ = len(l)
			else:
				f_calc(l)
			sum_all += sum_
		return
	elif isinstance(i, str):
		sum_all += len(i)
		return
	elif isinstance(i, int):
		sum_all += i
		return
	elif isinstance(i, dict):
		for d in i.keys():
			sum_all += d.__len__()
		sum_all += sum(i.values())
		return
	elif isinstance(i, tuple):
		sum_tuple(i)
	elif isinstance(i, set):
		sum_set(i)
	else:
		print(type(i), " not calculated.", i)


def sum_tuple(t):
	# sum_all += sum_
	for i in t:
		f_calc(i)
	print('tuple', t)
	return 0


def sum_set(_set):
	for i in _set:
		f_calc(i)
	print('set', i)
	return 0


def calculate_structure_sum(data_structure):
	global sum_all
	for i in data_structure:
		f_calc(i)

	return sum_all


# Увидев это студент задался вопросом: "А есть ли универсальное решение для
# подсчёта суммы всех чисел и длин всех строк?"
# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
result = calculate_structure_sum(data_structure)
print("---------------------------\nALL = ", result)
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... +
# 35 = 99
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.
