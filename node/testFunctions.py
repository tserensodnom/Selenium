from selenium.webdriver import ActionChains
from time import sleep
startDate = '10/10/2020'
finishData = '10/10/2021'
detailInfo = 'Deteiled info of Node'
tasks = ['Task','Project','Division','Other']
status = ['Not-started','In-progress','Done','Verified']
priority = ['Low','Medium','High','Urgent']
dependentFrom = 'user0'

def createNode (driver):
    previuosNode = driver.find_elements_by_class_name('mindmap-node')
    actionChains = ActionChains(driver)
    rigthclickElement = driver.find_elements_by_class_name('badge')
    actionChains.context_click(rigthclickElement[1]).perform()
    sleep(1)

    driver.find_element_by_xpath('//*[@id="create"]').click()

    driver.find_element_by_xpath('//*[@id="basicName"]').send_keys('Node 1')

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

