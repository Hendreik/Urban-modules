# module_10_3.py
"""
Блокировки и обработка ошибок
balance - баланс банка (int)
lock - объект класса Lock для блокировки потоков.
Метод deposit:
Будет совершать 100 транзакций пополнения средств.
Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
Метод take:
Будет совершать 100 транзакций снятия.
Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
В начале должно выводится сообщение "Запрос на <случайное число>".
Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив
 balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и заблокировать
 поток методом acquiere.
"""
from time import sleep
from random import randint


class Bank():
	TRAN = 100
	R1 = 5
	R2 = 500
	s3 = "Запрос отклонён, недостаточно средств"
	_delay = 0.001

	def __init__(self):
		self.balance = 0
		self.lock_deposit = Lock()
		self.lock_take = Lock()

	def deposit(self):

		with self.lock_deposit:
			n_in = randint(self.R1, self.R2)
			self.balance += n_in
			print(f'Пополнение: {n_in}. Баланс: {self.balance}')
			sleep(self._delay)

	def take(self):

		n_out = randint(self.R1, self.R2)
		print(f"Запрос на {n_out}")

		try:
			self.lock_take.acquire()
			if n_out > self.balance:
				print(self.s3)
				print('locked')
				while self.lock_take.locked():
					self.deposit()
					if self.balance > self.R2:
						# self.lock_take.release()
						print('unlock')
						break
			else:
				self.balance -= n_out
				print(f"Снятие: {n_out}. Баланс: {self.balance}")
		finally:
			self.lock_take.release()
#


from threading import Thread, Lock

bk = Bank()


def main():
	# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
	th1 = Thread(target=Bank.deposit, args=(bk,))
	th2 = Thread(target=Bank.take, args=(bk,))

	threads = []
	threads.extend([th1, th2])

	th1.start()
	th2.start()

	th1.join()
	th2.join()


tran = 1
while tran < bk.TRAN + 1:
	main()
	tran += 1

print(f'Итоговый баланс: {bk.balance}')
