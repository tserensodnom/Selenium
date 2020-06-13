import random
import string
from selenium.webdriver import ActionChains

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def split(word):
    return [char for char in word]

def edit(driver,nodes):
    actionChains = ActionChains(driver)
    actionChains.context_click(nodes[1]).perform()
    driver.find_element_by_xpath('//*[@id="update"]').click()

