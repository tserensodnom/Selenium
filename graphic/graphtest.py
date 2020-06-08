import unittest
from time import sleep
from selenium import webdriver
from graphic.AllFunctionsGraph import createGraphic
from graphic.AllFunctionsGraph import deleteGraphic,editGraphic,chooseGraphic,highlight
import sys
sys.path.append('Code project1/user/AllfuncionsUser')
from user.allfunctionsUser import logIn

class graphTest(unittest.TestCase):

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
        createGraphic(self.driver)
        #deleteGraphic(self.driver)
        #editGraphic(self.driver)
        #chooseGraphic(self.driver)
        #highlight(self.driver)
        sleep(3)
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()
