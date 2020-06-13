from selenium.webdriver import ActionChains
from time import sleep
from utils.functions import randomString,edit
nodeName = randomString(5)
startDate = '10/10/2020'
finishData = '10/10/2021'
detailInfo = 'Deteiled info of Node'
tasks = ['Task','Project','Division','Other']
status = ['Not-started','In-progress','Done','Verified']
priority = ['Low','Medium','High','Urgent']
dependentFrom = 'user0'
comment = randomString(5)
xOffset = 30
yOffset = 40

def createNode (driver):
    previuosNode = driver.find_elements_by_class_name('mindmap-node')
    actionChains = ActionChains(driver)
    rigthclickElement = driver.find_elements_by_class_name('badge')
    actionChains.context_click(rigthclickElement[1]).perform()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="create"]').click()
    driver.find_element_by_xpath('//*[@id="basicName"]').send_keys(nodeName)
    date = driver.find_elements_by_css_selector('#date')
    date[0].send_keys(startDate)
    date[1].send_keys(finishData)
    driver.find_element_by_css_selector('#basicTextarea').send_keys(detailInfo)

    selects = driver.find_elements_by_id('basicSelect')
    selects[0].click()
    for option in selects[0].find_elements_by_tag_name('option'):
        if option.text == tasks[2]:
            option.click()  # select() in earlier versions of webdriver
            break
    sleep(1)

    selects[1].click()
    for option in selects[1].find_elements_by_tag_name('option'):
        if option.text == status[0]:
            option.click()  # select() in earlier versions of webdriver
            break
    sleep(1)

    selects[2].click()
    for option in selects[2].find_elements_by_tag_name('option'):
        if option.text == priority[3]:
            option.click()  # select() in earlier versions of webdriver
            break
    sleep(2)

    fields = driver.find_elements_by_tag_name('input')
    fields[4].send_keys(dependentFrom)
    fields[5].click()
    sleep(2)

    searchGraph = driver.find_elements_by_class_name('vs__dropdown-menu')
    searchGraphtext = searchGraph[0].text
    textList = searchGraphtext.split("\n")
    fields[5].send_keys(textList[0])
    searchGraph[0].click()
    gotoGraph = driver.find_elements_by_class_name('col-4')
    #gotoGraph[0].click()
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[2].click()
    sleep(2)
    currentNode = driver.find_elements_by_class_name('mindmap-node')
    assert (len(currentNode) > len(previuosNode)), 'Create node failed'

def deleteNode(driver):
    previuosNode = driver.find_elements_by_class_name('mindmap-node')
    actionChains = ActionChains(driver)
    nodes = driver.find_elements_by_class_name('mindmap-node')
    actionChains.context_click(nodes[1]).perform()
    driver.find_element_by_xpath('//*[@id="delete"]').click()
    sleep(1)
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[1].click()
    sleep(2)
    currentNode = driver.find_elements_by_class_name('mindmap-node')
    assert (len(previuosNode) > len(currentNode)), 'Delete node failed'

def addComment(driver):
    previuosNode = driver.find_elements_by_class_name('mindmap-node')
    actionChains = ActionChains(driver)
    nodes = driver.find_elements_by_class_name('mindmap-node')
    actionChains.context_click(nodes[1]).perform()
    driver.find_element_by_xpath('//*[@id="update"]').click()
    commentField = driver.find_elements_by_tag_name('textarea')
    commentField[1].send_keys(comment)
    AddCommBtn = driver.find_element_by_class_name('btn-success').click()
    sleep(2)
    xBtn = driver.find_elements_by_class_name('close')
    xBtn[1].click()
    commentText = driver.find_elements_by_class_name('card-text')
    assert(comment == commentText[len(commentText) - 1].text), 'Add comment failed'
    sleep(1)

def Dependencies(driver):
    nodes = driver.find_elements_by_class_name('mindmap-node')
    edit(driver,nodes)
    fields = driver.find_elements_by_tag_name('input')
    dependentFrom = nodes[2].text
    dependentNode = dependentFrom.split(" ")
    fields[4].send_keys(dependentNode[0])
    list = driver.find_element_by_class_name('ti-item')
    list.click()
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[2].click()
    sleep(2)
    nodes = driver.find_elements_by_class_name('mindmap-node')
    edit(driver,nodes)
    sleep(1)
    checkElem = driver.find_element_by_class_name('ti-tag-center')
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[2].click()
    assert (checkElem.text == dependentNode[0]),'Dependencies failed'
    sleep(1)

def Deadline (driver):
    nodes = driver.find_elements_by_class_name('mindmap-node')
    edit(driver,nodes)
    date = driver.find_elements_by_css_selector('#date')
    date[0].send_keys(startDate)
    date[1].send_keys(finishData)
    sleep(1)
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[2].click()
    sleep(1)
    edit(driver,nodes)
    sleep(1)
    dateCurrent = driver.find_elements_by_class_name('form-control')
    currentStartdate = dateCurrent[1].get_attribute('value')
    currentStartdate = currentStartdate.split("-")
    oldStartDate = startDate.split("/")
    currentFinishdate = dateCurrent[2].get_attribute('value')
    currentFinishdate = currentFinishdate.split("-")
    oldFinishdate = finishData.split("/")
    assert (currentStartdate[0] == oldStartDate[2] and currentStartdate[1] == oldStartDate[1] and currentStartdate[2] == oldStartDate[0]), 'Deadline failed'
    assert (currentFinishdate[0] == oldFinishdate[2] and currentFinishdate[1] == oldFinishdate[1] and currentFinishdate[2] == oldFinishdate[0]), 'Deadline failed'
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[2].click()

def changePosition (driver):
    nodes = driver.find_elements_by_class_name('mindmap-node')
    changeElement = nodes[2]
    print(changeElement.location)
    previousPosition = changeElement.location
    ActionChains(driver).drag_and_drop_by_offset(changeElement, xOffset, yOffset).perform()
    currentPosition = changeElement.location
    assert (previousPosition != currentPosition), 'Change position failed'
    sleep(1)
