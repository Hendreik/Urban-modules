#  tests_12_1.py
"""
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого
 объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого
 объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов
 вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
  чтобы убедится в неравенстве результатов.
"""
import runner as r
import unittest

class RunnerTest(unittest.TestCase):
	def test_walk(self):
		self.r1=r.Runner("m")
		for i in range(0, 10):
			self.r1.walk()
		self.assertEqual(self.r1.distance,50)
		return

	def test_run(self):
		self.r1=r.Runner("m")
		for i in range(0, 10):
			self.r1.run()
		self.assertEqual(self.r1.distance,100)
	def test_challenge(self):
		self.r1=r.Runner("m")
		self.r2=r.Runner("n")
		for i in range(0, 10):
			self.r1.walk()
			self.r2.run()
		self.assertNotEqual(self.r1.distance,self.r2.distance,"Equal")

if __name__ == "__main__":
	unittest.main()
