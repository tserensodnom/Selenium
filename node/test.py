import unittest
import json
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
        driver.get('https://auth.bolor.net/login?t=MindTask')
        driver.maximize_window()
        self.driver = driver

    def runTest(self):
        with open(r'/home/tserensodnom/Desktop/Uulzal project/Code project1/user/config.json') as f:
            data = json.load(f)
        logIn(self.driver, data['login'])
        with open(r'/home/tserensodnom/Desktop/Uulzal project/Code project1/node/config.json') as f:
            data1 = json.load(f)
        for elem in data1:
            if elem == "create_node":
                sleep(0.5)
                createNode(self.driver, data1['create_node'])
            elif elem == "delete_node":
                sleep(0.5)
                deleteNode(self.driver, data1['delete_node'])
            elif elem == "add_comment":
                sleep(0.5)
                addComment(self.driver, data1['add_comment'])
            elif elem == "dependencies":
                 Dependencies(self.driver, data1['dependencies'])
            elif elem == "change_position":
                sleep(0.1)
                changePosition(self.driver, data1['change_position'])
            elif elem == "deadline":
                Deadline(self.driver, data1['deadline'])
        sleep(3)
        self.driver.quit()        # logIn(self.driver)
if __name__ == '__main__':
    unittest.main()