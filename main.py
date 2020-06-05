import unittest
from user.usertest import userTest
from time import sleep
from graphic.graphtest import graphTest
from node.nodetest import nodeTest

tUser = unittest.TestLoader().loadTestsFromTestCase(userTest)
#tGraph = unittest.TestLoader().loadTestsFromTestCase(graphTest)
#tNode = unittest.TestLoader().loadTestsFromTestCase(nodeTest)

test1 = unittest.TestSuite([tUser])
#test2 = unittest.TestSuite([tGraph])
#test3 = unittest.TestSuite([tNode])

unittest.TextTestRunner(verbosity=2).run(test1)
#unittest.TextTestRunner(verbosity=2).run(test2)
#unittest.TextTestRunner(verbosity=2).run(test3)

