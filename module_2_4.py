#
# module_2_4.py
#  "Цикл for. Элементы списка. Полезные функции в цикле"
#  Цель: закрепить навык решения задач при помощи цикла for, применив
# знания об основных типах данных.

#  Задача "Всё не так уж просто":
#  Дан список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
Kol = len(numbers)
primes = []  # простые
not_primes = []  # не простые
dict_ = dict({})
for i in range(Kol):
	nn = numbers[i]
	if nn == 1: continue  # 1 не является ни простым, ни составным
	is_prime = True
	#
	for j in range(2, nn):
		if nn % j == 0:
			is_prime = False  # флаг
			break

	if is_prime:
		primes.append(nn)
	else:
		not_primes.append(nn)
	dict_[nn] = is_prime
#
print(f'простые: ', primes)
print(f'не простые: ', not_primes)
print(f'all ', dict_)
