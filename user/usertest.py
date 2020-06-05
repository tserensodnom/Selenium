import unittest
from time import sleep
from selenium import webdriver
from .AllfunctionsUser import createAccount, logIn
from .AllfunctionsUser import logOut, basicInfo, changePassword


class userTest(unittest.TestCase):

    def __init__(self,name):
        super().__init__()
        driver = webdriver.Chrome(
            '/home/tserensodnom/Downloads/chromedriver_linux64/chromedriver')  # Optional argument, if not specified will search path.
        driver.implicitly_wait(30)
        driver.get('http://www.uulzalt.com:8001/')
        driver.maximize_window()
        self.driver = driver

    def runTest(self):
       # createAccount(self.driver)
        logIn(self.driver)
        logOut(self.driver)
        logIn(self.driver)
        basicInfo(self.driver)
        changePassword(self.driver)
        logOut(self.driver)
        logIn(self.driver)
        sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
