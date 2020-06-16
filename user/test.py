import unittest
from time import sleep
from selenium import webdriver
from .functions import createAccount, logIn
from .functions import logOut, basicInfo, changePassword

sequence = [ #TODO change procedure order
    "createAccount",
    "logIn",
    "logOut",
    "logIn",
    "basicInfo",
    "changePassword",
    "logOut",
    "logIn",
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
        # logIn(self.driver)
        # logOut(self.driver)
        # logIn(self.driver)
        # basicInfo(self.driver)
        # changePassword(self.driver)
        # logOut(self.driver)
        # logIn(self.driver)
        for elem in sequence:
            #getattr(self,elem)(self.driver)
            print(elem)
            #elem(self.driver)
            if elem == "logIn":
             logIn(self.driver)
            elif elem == "createAccount":
                createAccount(self.driver)
            elif elem == "logOut":
                logOut(self.driver)
            elif elem == "basicInfo":
                basicInfo(self.driver)
            elif elem == "changePassword":
                changePassword(self.driver)
        sleep(3)
        self.driver.quit()

# def _runTest(self): #array of string
    #     for elem in sequence:
    #         getattr(self, elem)(self.driver) #TODO Dynamic Programming zuvhun functionuud usertestiinh bhad ahiglaj boloh bsn
    #         if elem == "logIn":
    #             logIn(self.driver)

if __name__ == "__main__":
    unittest.main()
