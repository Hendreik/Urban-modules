import os
import time

directory = "."
os.chdir(directory)
print(os.getcwd())
n=0
print("-" * 10)

for root, dirs, files in os.walk(directory):
	print(root, dirs, files)
	n +=1
	if n ==5: break

print("_"*10)
n=0
file_last = None
for root, dirs, files in os.walk(directory):
	n +=1
	if n ==5: break
	for file in files:
		filepath = os.path.join(root, file)
		if not filepath.endswith('.py'):
			continue
		file_last = file.title()
		with open(filepath, 'r', encoding='utf-8') as file:
			print(filepath)
			filepath_ = filepath
			parent_dir = root
			for line in file:
				if line.__contains__('def'):
					print(">>> ", line)
					break

print("*"*10)
print(file_last, file_last.__getstate__())
formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(file_last)))
filesize = os.path.getsize(file_last)
print(f'Обнаружен файл: {file_last}, Путь: {filepath_}, Размер: {filesize} байт,'
	  f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

print("-" * 10)
print(os.listdir())
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)
n=0
for j in os.walk('.'):
	n += 1
print(n)
