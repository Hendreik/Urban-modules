# tests_12_4.py
"""
Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
"""
import rt_with_exceptions as rte
import logging
class RunnerTest():
	def test_walk(self,name, speed):
		try:
			r1= rte.Runner(name, speed)
			for _ in range(10):
				r1.walk()

			logging.info(f"test_walk выполнен успешно. runner {name} accelerated speed {speed}")

		except Exception as e:
			logging.warning(f"Неверная скорость для Runner. incorrect data. name: {name} speed: {speed}",exc_info=True)
			#raise ValueError
			return -1

	def test_run(self, name):
		try:
			r1=rte.Runner(name)
			for _ in range(0, 10):
				r1.run()

			logging.info(f"test_run выполнен успешно. runner {name}")

		except BaseException as e:
			#print(e.__str__())
			logging.warning(f"Неверный тип данных для объекта Runner. incorrect data: name: {name}",exc_info=True)
			return -2


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
	encoding=' UTF-8', format="%(asctime)s || %(levelname)s || %(message)s")

r= RunnerTest()

r.test_walk("mick",160)
r.test_walk("mick",-160)
r.test_run("mick")
r.test_run(160)
