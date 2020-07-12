from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.functions import randomString, edit, engine
nodeName = randomString(5)

def createNode(driver, data):
    preNode = driver.find_elements_by_class_name('mindmap-node')
    edit(driver,x='add', i = 0)
    engine(driver,data)
    selects = driver.find_elements_by_id('basicSelect')
    for elem in selects:
        if elem == selects[0]:
            continue
        else:
            elem.click()
            for option in elem.find_elements_by_tag_name('option'):
                for element in data:
                    if element['path'] == None:
                        if option.text == element['value']:
                            option.click()  # select() in earlier versions of webdriver
                            break
            sleep(2)
    okBtn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/button[2]')
    okBtn.click()
    sleep(2)
    curNode = driver.find_elements_by_class_name('mindmap-node')
    assert (len(preNode) < len(curNode)), 'Create node faileds'

def deleteNode(driver,data):
    preNode = driver.find_elements_by_class_name('mindmap-node')
    edit(driver, x = 'delete', i = 1)
    engine(driver,data)
    curNode = driver.find_elements_by_class_name('mindmap-node')
    assert (len(preNode) > len(curNode)), 'Delete node failed'

def addComment(driver,data):
    edit(driver, x = 'edit', i = 1)
    engine(driver,data)
    checkText = driver.find_elements_by_class_name('card-text')
    assert (checkText[len(checkText) - 1].text == data[0]['value']), 'Add comment failed'
    xbtn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/header/button')
    xbtn.click()

def Dependencies(driver,data):
    nodes = driver.find_elements_by_class_name('mindmap-node')
    print(nodes[1].text)
    edit(driver, x='edit', i=1)
    fill = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[1]/form[2]/div[4]/div/div/div/ul/li/input')
    text = nodes[2].text
    text = text.split('\n')
    print(text)
    fill.send_keys(text[0])
    okBtn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/button[2]')
    okBtn.click()
    edit(driver, x='edit', i=1)
    sleep(1)
    # nodes = driver.find_elements_by_class_name('mindmap-node')
    # edit(driver,nodes)
    # fields = driver.find_elements_by_tag_name('input')
    # dependentFrom = nodes[2].text
    # dependentNode = dependentFrom.split(" ")
    # fields[4].send_keys(dependentNode[0])
    # list = driver.find_element_by_class_name('ti-item')
    # list.click()
    # okBtn = driver.find_elements_by_class_name('btn-primary')
    # okBtn[2].click()
    # sleep(2)
    # nodes = driver.find_elements_by_class_name('mindmap-node')
    # edit(driver,nodes)
    # sleep(1)
    # checkElem = driver.find_element_by_class_name('ti-tag-center')
    # okBtn = driver.find_elements_by_class_name('btn-primary')
    # okBtn[2].click()
    # assert (checkElem.text == dependentNode[0]),'Dependencies failed'
    # sleep(1)

def Deadline (driver,data):
    edit(driver,x='edit', i=1)
    engine(driver,data)
    edit(driver,x='edit', i=1)
    startDate = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div/form[1]/div[2]/div/input')
    finishDate = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div/form[1]/div[3]/div/input')
    assert (startDate.get_attribute('value') == data[0]['value1'] and
            finishDate.get_attribute('value') == data[1]['value1']), 'Deadline failed'
    sleep(1)
    xbtn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/button[1]')
    xbtn.click()

def changePosition (driver,data):
    nodes = driver.find_elements_by_class_name('mindmap-node')
    # ActionChains(driver).drag_and_drop_by_offset(nodes[0], data[0]['xoffset'], data[0]['yoffset']).perform()
    # ActionChains(driver).drag_and_drop_by_offset(nodes[1], data[0]['xoffset'], data[0]['yoffset']).perform()
    # driver.implicitly_wait(100)
    #ActionChains(driver).drag_and_drop_by_offset(nodes[2], data[0]['xoffset'], data[0]['yoffset']).perform()
    # ActionChains(driver).drag_and_drop_by_offset(nodes[3], data[0]['xoffset'], data[0]['yoffset']).perform()

    # for idx, elem in enumerate(nodes):
    #     # prePosition = elem.location
    #     sleep(2)
    #     ActionChains(driver).drag_and_drop_by_offset(elem, 10, 5).perform()
    #     sleep(2)
    # sleep(1)

    # nodes = driver.find_elements_by_class_name('mindmap-node')
    # changeElement = nodes[2]
    # print(changeElement.location)
    # previousPosition = changeElement.location
    # ActionChains(driver).drag_and_drop_by_offset(changeElement, xOffset, yOffset).perform()
    # currentPosition = changeElement.location
    # assert (previousPosition != currentPosition), 'Change position failed'
    # sleep(1)
