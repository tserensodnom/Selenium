import unittest
from user.test import UserTest
from time import sleep
from graphic.test import GraphTest
from node.test import NodeTest

tests = [
    UserTest,
    # GraphTest,
    # NodeTest
]
for test in tests:
    testSuite = unittest.TestLoader().loadTestsFromTestCase(test)
    unittest.TextTestRunner(verbosity=2).run(testSuite)
