# suite_12_3.py
"""
 "Заморозка кейсов"
 RunnerTest
 TournamentTest
"""
import unittest
import tests_12_1 as t1
import tests_12_2 as t2

ts1= unittest.TestSuite()
ts1.addTest(unittest.TestLoader().loadTestsFromTestCase(t1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(ts1)

ts2= unittest.TestSuite()
ts2.addTest(unittest.TestLoader().loadTestsFromTestCase(t2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(ts2)

