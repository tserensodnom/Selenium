import unittest
from selenium import webdriver
from time import sleep
from .functions import createNode ,deleteNode,addComment,Dependencies,Deadline,changePosition
from user.functions import logIn

class NodeTest(unittest.TestCase):
    def __init__(self,name):
        super().__init__()
        driver = webdriver.Chrome(
            '/home/tserensodnom/Downloads/chromedriver_linux64/chromedriver')  # Optional argument, if not specified will search path.
        driver.implicitly_wait(30)
        driver.get('http://www.uulzalt.com:8001/')
        driver.maximize_window()
        self.driver = driver

    def runTest(self):
        logIn(self.driver)
        #createNode(self.driver)
        #deleteNode(self.driver)
        #addComment(self.driver)
        #Dependencies(self.driver)
        #Deadline(self.driver)
        changePosition(self.driver)
        sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()