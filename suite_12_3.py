import unittest
import Module_12_3 as M123

test = unittest.TestSuite
test.addTest(unittest.TestLoader().loadTestsFromTestCase(M123.RunnerTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(M123.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test)

