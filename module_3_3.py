#
# module_3_3.py
# по уроку "Распаковка позиционных параметров".
def print_params(a=1, b='строка', c=True):
	print(a, b, c)

# Создайте список
values_list = [-111, False, 'name', [11, 12, 13]]  # с тремя элементами разных типов.
# Создайте словарь
values_dict = {'N1': 333, "N2": 444, 'a': -1, 'b': 0, 'c': 1}

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print_params(values_list)
print_params(*values_list[3])
print_params(values_list[0], values_list[2], False)
print_params(4, 5, 6)

# Создайте список
values_list_2 = ['par1', {'n1': 22, 'n2': 32}]  # с двумя элементами разных типов
print_params(a=values_list[0], b=values_list_2[0], c=values_list_2[1].values())
# Проверьте, работает ли print_params(*values_list_2, 42)
# Пример результата выполнения программы:
# Исходный код:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

# -------------------------
# Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
# В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
# def a(my_list = [])) – это приводит к ошибкам!

# Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
# def append_to_list(item, list_my=None):
#   if list_my is None:
#    list_my = []
#   list_my.append(item)
# print(list_my)
