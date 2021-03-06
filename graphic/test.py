import unittest
import json
from time import sleep
from selenium import webdriver
from graphic.functions import createGraphic, searchButton
from graphic.functions import deleteGraphic, editGraphic, chooseGraphic, highlight
from user.functions import logIn
from utils.functions import randomString


class GraphTest(unittest.TestCase):
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
            elif elem == "choose_graphic":
                chooseGraphic(self.driver, data1['choose_graphic'])
            elif elem == "delete_graphic":
                deleteGraphic(self.driver, data1["delete_graphic"])
            elif elem == "edit_graphic":
                editGraphic(self.driver, data1['edit_graphic'])
            elif elem == "search_button":
                searchButton(self.driver, data1['search_button'])
            elif elem == "hightlight":
                highlight(self.driver, data1['hightlight'])
        sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
