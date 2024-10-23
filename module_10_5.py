# module_10_5.py
"""
Задача "Многопроцессное считывание":
Создайте функцию read_info(name), где name - название файла. Функция должна:
Создавать локальный список all_data.
Открывать файл name для чтения.
Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
Во время считывания добавлять каждую строку в список all_data.
"""
import os
import multiprocessing as mp
import datetime as dt
import threading as th


def _read_info2(name):
	print(name)
	all_data = []
	with open(name, 'r') as file:
		for line in file:
			all_data.append(line)
			if line == "":
				break

	for i in range(0, 10):
		print(all_data[i])


def read_info(name):
	print(name)
	th.Thread(target=read_(name), args=(name,)).start()


def read_(name):
	all_data = []
	line_ = "0"
	with open(name, 'r') as file:
		while not line_ in ("", "/n"):
			line_ = file.readline()
			all_data.append(line_)
			if line_ == "":
				break

	for i in range(0, 10):
		print(all_data[i])


def main_proc():
	dir_ = f'./Files/'
	files_ = []
	for f in os.listdir(dir_):
		files_.append(dir_ + f)

	filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
	time_start = dt.datetime.now()
	# Линейный вызов
	for f in files_:
		read_info(f)
	time_end = dt.datetime.now()
	print('all time is ', time_end - time_start)

	# Многопроцессный
	time_start2 = dt.datetime.now()
	with mp.Pool(processes=4) as pool:
		pool.map(_read_info2, filenames)

	time_end2 = dt.datetime.now()

	print("	# Линейный вызов")
	print('all time is ', time_end - time_start)
	print("	# Многопроцессный")
	print('all time is ', time_end2 - time_start2)
	return 0


# -----------------


if __name__ == '__main__':
	try:
		main_proc()
	except BaseException as e:
		print({e.__context__})
