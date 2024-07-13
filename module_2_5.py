#module_2_5.py
# "Функции в Python.Функция с параметром"
# Цель: закрепить навык написания функций и их вызовов.
#
# Задача "Матрица воплоти":
def get_matrix(n=0, m=0, value=0):
	#размерами n строк и m столбцов, заполненную значениями value
	#Создайте пустой список
	matrix = []
	mt = []
	if 0 in (n,m) or n<0 or m<0: 	print('matrix')
	else:
		for i in range(m): mt.extend([value])
		for i1 in range(n):
			matrix.extend([mt])
	return matrix

print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
