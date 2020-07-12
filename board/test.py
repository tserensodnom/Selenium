import unittest
import json
from selenium import webdriver
from time import sleep
from board.functions import drag
from utils.functions import randomString
from user.functions import logIn
from graphic.functions import createGraphic
from node.functions import createNode


class BoardTest(unittest.TestCase):
    def __init__(self, name):
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
        with open(r'/home/tserensodnom/Desktop/Uulzal project/Code project1/graphic/config.json') as f:
            data1 = json.load(f)
        for elem in data1:
            if elem == "create_graphic":
                for item in data1['create_graphic']:
                    if item['value'] != None:
                        item['value'] = randomString(5)
                        with open('/home/tserensodnom/Desktop/Uulzal project/Code project1/graphic/config.json',
                                  'w') as f:
                            json.dump(data1, f, indent=2)
                createGraphic(self.driver, data1['create_graphic'])
        with open(r'/home/tserensodnom/Desktop/Uulzal project/Code project1/board/config.json') as f:
            data2 = json.load(f)
        for elem in data2:
            if elem == "create_node":
                i = 0
                while i < 5:
                    for idx, item in enumerate(data2['create_node']):
                        if idx == 0:
                            item['value'] = randomString(5)
                            with open('/home/tserensodnom/Desktop/Uulzal project/Code project1/board/config.json',
                                      'w') as f:
                                json.dump(data2, f, indent=2)
                            break
                        else:
                            break
                    createNode(self.driver, data2['create_node'])
                    i += 1
            elif elem == "drag":
                drag(self.driver, data2['drag'])
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
