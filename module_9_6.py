# module_9_6.py
"""
Генераторы

"""


def all_variants1(text):
	for n in text:
		yield n


def all_variants(text):
	for n in text:
		yield n
	for i in range(len(text) - 1):
		yield text[i] + text[i + 1]
	yield text[0:]


string_ = 'Напишите функцию-генератор all_variants(text)'

for s in all_variants1(string_):
	print(s, end='')
print()
for s in all_variants('abc'):
	print(s)
print()
for s in all_variants('abcv'):
	print(s)
