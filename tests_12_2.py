#  tests_12_2
"""
setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
tearDownClass - метод, где выводятся all_results по очереди в столбец.
"""
import runner_and_tournament as rt
import unittest

class TournamentTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.all_results={}
	def setUp(self):
		self.runner1=rt.Runner('Усэйн',10)
		self.runner2=rt.Runner('Андрей',9)
		self.runner3=rt.Runner('Ник',3)

	def test_run1(self):
		self.t = rt.Tournament(90,self.runner1, self.runner3)
		self.all_results=self.t.start()
		self.assertTrue(self,self.runner3 == self.all_results.get(2))
	def test_run2(self):
		self.t = rt.Tournament(90,self.runner2, self.runner3)
		self.all_results=self.t.start()
		self.assertTrue(self,self.runner3 == self.all_results.get(2))
	def test_run3(self):
		self.t = rt.Tournament(90,self.runner1, self.runner2, self.runner3)
		self.all_results=self.t.start()
		self.assertTrue(self,self.runner3 == self.all_results.get(3))
	def test_down(self):
		self.t = rt.Tournament(90,self.runner1, self.runner2, self.runner3)
		self.all_results=self.t.start()
		for key, value in self.all_results.items():
			print(key, value)

	@classmethod
	def tearDownClass(cls):
		for key,value in cls.all_results.items():
			print(key,value)


if __name__ == "__main__":
	unittest.main()
