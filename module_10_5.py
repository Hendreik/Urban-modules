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
import multiprocessing

dir_ = f'../Files'
files_ = []
for f in os.listdir(dir_):
	files_.append(f)


def read_info(name):
