import random
import string
from time import sleep
from selenium.webdriver import ActionChains

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def split(word):
    return [char for char in word]

def edit(driver, x, i):
   if x == 'edit':
       nodes = driver.find_elements_by_class_name('mindmap-node')
       actionChains = ActionChains(driver)
       actionChains.context_click(nodes[i]).perform()
       driver.find_element_by_xpath('').click()
   elif x == 'add':
       nodes = driver.find_elements_by_class_name('mindmap-node')
       actionChains = ActionChains(driver)
       actionChains.context_click(nodes[i]).perform()
       driver.find_element_by_xpath('//*[@id="create"]').click()
   elif x == 'delete':
       nodes = driver.find_elements_by_class_name('mindmap-node')
       actionChains = ActionChains(driver)
       actionChains.context_click(nodes[i]).perform()
       driver.find_element_by_xpath('//*[@id="delete"]').click()

def engine(driver, data):
    for element in data:
        if element['clickable'] == True and element['filled'] == False and element['path'] != None:
            elem = driver.find_element_by_xpath(element['path'])
            sleep(2)
            elem.click()
            sleep(2)
        elif element['path'] != None:
            elem = driver.find_element_by_xpath(element['path'])
            elem.clear()
            elem.send_keys(element['value'])
            sleep(1.5)
    sleep(1.5)

