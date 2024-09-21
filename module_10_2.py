# module_10_2.py
"""
Потоки на классах
	name (str)
	power (int)
количество врагов уменьшается на power текущего рыцаря.
"""
import threading
from threading import Thread
from time import sleep


class Knight(Thread):
	ENEMY = 100
	_st1 = ", на нас напали!"

	def __init__(self, name, power):
		self.name_ = name
		self._power = power
		super().__init__()

	def run(self):
		try:
			print(f"{self.name_}{self._st1}")
			enemy = self.ENEMY
			days = 0
			while enemy > 0:
				enemy -= self._power
				days += 1
				print(f"{self.name_} сражается {days} days..., осталось {enemy} воинов.")
				sleep(1)
			st3 = f"{self.name_} одержал победу спустя {days} дней(дня)!"
			print(st3)
			self.ENEMY = 0

		except Exception as e:
			print(e.__str__())

	def ending(self):
		while self.ENEMY != 0:
			sleep(1)
		return self.ENEMY


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join(3)
second_knight.join(3)
# Вывод строки об окончании сражения
print(first_knight.name, first_knight.is_alive(), " alive")
print(second_knight.__getstate__(), second_knight.is_alive())

assert threading.active_count() == 2

print('All over', 'наши победили', first_knight.ending(), second_knight.ending())
