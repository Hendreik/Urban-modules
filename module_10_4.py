# module_10_4.py
"""
"Очереди для обмена данными между потоками."
"""
import time
from threading import Thread
from datetime import datetime as dt
from random import randrange
import queue


class Table:

	def __init__(self, number, guest=None):
		self.number = number
		self.guest = guest


class Guest(Thread):
	def __init__(self, name):
		super().__init__()
		self.name_guest = name
		self.sit = 0
		self.gone = 0
		self.state = ''

	def run(self):
		timing = randrange(3, 11)  # step,1)
		self.state = self.name_guest, timing, "сек."
		time.sleep(timing)


class Cafe:
	def __init__(self, *tables):
		self.tables = tables
		self.queue = None
		self.guests = []
		self.st = "сел(-а) за стол номер"

	def guest_arrival(self, *guests):
		self.guests = guests
		#		for g in guests[:len(self.tables)]:
		for g in guests:
			for tb in self.tables:
				if tb.guest == None:
					tb.guest = g
					g.sit = 1
					print(g.name_guest, self.st, tb.number)
					g.start()
					break
			if g.sit == 0:
				print(g.name_guest, "<имя гостя> в очереди")
				self.queue.put(item=[Table(0), g])

	def discuss_guests(self):

		for table in self.tables:
			guest = table.guest
			print(guest.state)
			is_alive = guest.is_alive()
			print(guest, is_alive, table.number)
			if not is_alive and table.number != 0:
				table.guest = None
				self.discuss_out(table, guest)
			guest.join()

	def discuss_out(self, table, guest):
		print(f"{guest.name_guest} <имя гостя за текущим столом> покушал(-а) и ушёл(ушла)")
		print(f"Стол номер {table.number} <номер стола> свободен")
		guest.sit, guest.gone = 0, 1

	def discuss(self):
		item = q.get()
		table = item[0]
		guest = item[1]
		print('--------------')
		#		print(guest.is_alive(),table.number, guest, table.guest		)
		if table.number == 0:
			self.discuss_out2(table, guest)

			if guest.sit == 0:
				self.disdiscuss()
				self.discuss_out2(table, guest)

			guest.join()

	def discuss_out2(self, table, guest):
		if table.number == 0:
			for t_ in self.tables:
				if t_.guest is None:
					self.st = f"<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
					t_.guest = guest
					guest.start()
					print(guest.state)
					table.number = t_.number
					print(guest.name_guest, self.st, t_.number)
					guest.sit, guest.gone = 1, 0
					#					guest.join()
					break

	def disdiscuss(self):
		for g in self.guests:
			if (not g.is_alive()) and g.sit == 1 and g.gone == 0:
				for t_ in self.tables:
					if t_.guest == g:
						t_.guest = None
						self.discuss_out(t_, g)
						g.sit, g.gone = 0, 1
						#						g.start()
						return


"""
Метод guest_arrival(self, *guests):
Должен принимать неограниченное кол-во гостей (объектов класса Guest).
Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
Метод discuss_guests(self):
Этот метод имитирует процесс обслуживания гостей.
Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
Далее запустить поток этого гостя (start)
Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
Table - стол, хранит информацию о находящемся за ним гостем (Guest).
Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).
"""
# Создание столов
tables = [Table(number) for number in range(1, 6)]
num_tables = 5
# Имена гостей
guests_names = [
	'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
	'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)

q = queue.Queue()
cafe.queue = q
cafe.guests = guests

# Приём гостей
try:
	cafe.guest_arrival(*guests)
	# Thread(target=cafe.guest_arrival(*guests), args=(q, *guests))

	# Обслуживание гостей
	# cafe.discuss_guests()
	Thread(target=cafe.discuss_guests(), args=(q,))
except Exception as e:
	print(e.__str__())

while not cafe.queue.empty():
	try:
		Thread(target=cafe.discuss(), args=(q,))
	#	Thread(target=cafe.disdiscuss(), args=(q,))
	except Exception as e:
		print(e.__str__())

print('ждём')
print('в очереди пусто:', cafe.queue.empty())

q.task_done()
