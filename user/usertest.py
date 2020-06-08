import unittest
from time import sleep
from selenium import webdriver
from .allfunctionsUser import createAccount, logIn
from .allfunctionsUser import logOut, basicInfo, changePassword


sequence = [ #TODO change procedure order
    "logIn",
    "logOut",
    "logIn",
    "logOut",

]


class UserTest(unittest.TestCase):

    def __init__(self, _):
        super().__init__()
        driver = webdriver.Chrome(
            '/home/tserensodnom/Downloads/chromedriver_linux64/chromedriver')
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

    # def _runTest(self): #array of string
    #     for elem in sequence:
    #         getattr(self, elem)(self.driver) #TODO Dynamic Programming zuvhun functionuud usertestiinh bhad ahiglaj boloh bsn
    #         if elem == "logIn":
    #             logIn(self.driver)


if __name__ == "__main__":
    unittest.main()
