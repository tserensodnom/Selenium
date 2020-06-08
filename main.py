import unittest
from user.usertest import UserTest
from time import sleep
from graphic.graphtest import graphTest
from node.nodetest import nodeTest

tests = [
    UserTest,
    graphTest,
    nodeTest
]
for test in tests:
    testSuite = unittest.TestLoader().loadTestsFromTestCase(test)
    unittest.TextTestRunner(verbosity=2).run(testSuite)
