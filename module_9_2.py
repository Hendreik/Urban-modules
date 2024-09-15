# module_9_2.py
"""
"Списковые, словарные сборки"
Задача:
Даны несколько списков, состоящих из строк
"""
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
"""
В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings, при
 условии, что длина строк не менее 5 символов.
В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины.
 Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина
 строки. Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings. Условие
  записи пары в словарь - чётная длина строки.
"""
first_result = \
	[len(s) for s in first_strings if len(s) > 4]
print(list(first_result))

second_result = \
	[(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]
print(second_result)

third_result = {}
[third_result.update({s: len(s)}) for s in first_strings + second_strings if not len(s) % 2]
print(third_result)
