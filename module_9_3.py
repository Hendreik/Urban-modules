#  module_9_3.py
"""
Генераторные сборки
Необходимо создать 2 генераторных сборки:
В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк в одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.
"""
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i) - len(j) for i, j in zip(first, second) if len(i) != len(j))
print(list(first_result))

second_result = (len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(len(second)) if i == j)

print(list((len(i) for i in first)))
n2 = (len(j) for j in second)
print(list(n2))

print(list(second_result))
