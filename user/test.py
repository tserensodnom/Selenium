import unittest
from time import sleep
from selenium import webdriver
import json
from .functions import createAccount, logIn, createCompany
from utils.functions import randomString
from .functions import logOut, basicInfo, changePassword, backHomepage


class UserTest(unittest.TestCase):
    def __init__(self, _):
        super().__init__()
        driver = webdriver.Chrome(
            '/home/tserensodnom/Downloads/chromedriver_linux64/chromedriver')
        driver.implicitly_wait(30)
        driver.get('https://auth.bolor.net/login?t=MindTask')
        driver.maximize_window()
        self.driver = driver
        sleep(2)

    def runTest(self):
        with open(r'/home/tserensodnom/Desktop/Uulzal project/Code project1/user/config.json') as f:
            data = json.load(f)
        for elem in data:
            if elem == "create":
                createAccount(self.driver, data['create'])
                print(data['create'])
            elif elem == "login":
                logIn(self.driver, data['login'])
            elif elem == "logOut":
                logOut(self.driver, data['logOut'])
                logIn(self.driver, data['login'])
            elif elem == "basic_info":
                basicInfo(self.driver, data['basic_info'])
            elif elem == "change_password":
                changePassword(self.driver, data['change_password'])
            elif elem == "back_to_home":
                backHomepage(self.driver, data['back_to_home'])
        sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
