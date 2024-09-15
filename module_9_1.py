# module_9_1.py
"""
"Введение в функциональное программирование"
Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
int_list - список из чисел (int, float)
*functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
Эта функция должна:
Вызвать каждую функцию к переданному списку int_list
Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком int_list.
Пункты задачи:
В функции apply_all_func создайте пустой словарь results.
Переберите все функции из *functions.
При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
Верните словарь results.
Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.
"""
int_list = [1, 2.02, 3, 4.4, -5, 6]

def func1(x):
	return x + 1

def func2(x):
	return x * 2

def func3(x):
	return x * x

funcs = [func1, func2, func3]


def _all_func(int_list, *functions):
	results = {}
	for f in functions:
		print(f.__name__)
		for i in int_list:
			results[i] = f(i)
		# print(f(i))
		print(results)

	return results


def apply_all_func(int_list, *functions):
	results = {}
	for f in functions:
		results[f.__name__] = f(int_list)

	return results


###
result = _all_func(int_list, *funcs)
print('----')
###
"""
min - принимает список, возвращает минимальное значение из него.
max - принимает список, возвращает максимальное значение из него.
len - принимает список, возвращает кол-во элементов в нём.
sum - принимает список, возвращает сумму его элементов.
sorted - принимает список, возвращает новый отсортированный список на основе переданного.
"""
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
