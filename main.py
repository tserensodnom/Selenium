import unittest
from user.test import UserTest
from graphic.test import GraphTest
from node.test import NodeTest
from board.test import BoardTest

tests = [
    #UserTest,
    #GraphTest,
    #NodeTest,
    BoardTest
]
for test in tests:
    testSuite = unittest.TestLoader().loadTestsFromTestCase(test)
    unittest.TextTestRunner(verbosity=2).run(testSuite)

