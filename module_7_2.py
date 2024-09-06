# module_7_2.py
"""
Позиционирование в файле
Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
 strings - список строк для записи.
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением -
 записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
"""
from pprint import pprint

file_name = "FILE.txt"
strings = [
	'string 1', 'string 2', 'string 3', 'string 4', 'string 5', 'string 6'
]


def custom_write(file_name, strings):
	strings_positions = {}
	it = iter(strings)

	file = open(file_name, 'tw+', -1, 'utf-8', newline='\n')
	t = file.tell()

	for i in range(strings.__len__()):
		strings_positions.update({(i + 1, t): strings[i]})
		file.write(next(it) + '\n')
		t = file.tell() + 1

	file.close()
	#
	# file = open(file_name)
	# st1=''
	# st1 += file.read()
	# file.close()
	# print(st1)

	return strings_positions


###
s = custom_write(file_name, strings)

pprint(s)
