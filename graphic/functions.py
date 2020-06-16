from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

newGraphicName = 'New graph 1'
aboutText = 'dkghkj jgkljglkhag  kjlhgklah jklgjlka j'
chooseGraphicNumber = '1'
deleteGraphicNumber = '2'
changeGraphicName = 'Change name'
changeGraphicAbout = 'Change about'
sum = 0
newGraphicNumber = 0

def graphicNumber (driver):
    WebDriverWait(driver, 10).until(  # Click menu button
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    WebDriverWait(driver, 10).until(  # Click select button in menu
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[3]'))).click()
    sleep(1)
    tabs = driver.find_elements_by_class_name('page-link')
    sum = 0
    for i in range(len(tabs) - 2):
        graphNumber = driver.find_elements_by_tag_name('tr')
        sum += len(graphNumber)
        if i == (len(tabs) - 3):
            break
        else:
            tabs[len(tabs) - 1].click()
            sleep(1)
    sleep(1)
    xBtn = driver.find_elements_by_class_name('close')
    xBtn[1].click()
    sleep(1)
    return sum

def createGraphic (driver):
    PreviosGraphicNumber = graphicNumber(driver)
    print('PreviosGraphicNumber',PreviosGraphicNumber)
    WebDriverWait(driver, 10).until(  # Click menu button
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    sleep(1)
    WebDriverWait(driver, 10).until(  # Click create graph button in menu
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[2]'))).click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="basicName"]').send_keys(newGraphicName)
    driver.find_element_by_id('basicTextarea').send_keys(aboutText)
    sleep(1)
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[1].click()
    sleep(2)
    CurrentGraphicNumber = graphicNumber(driver)
    print('CurrentGraphicNumber',CurrentGraphicNumber)
    assert (PreviosGraphicNumber < CurrentGraphicNumber), 'Create graphic failed'

def chooseGraphic (driver):
    WebDriverWait(driver, 10).until(  # Click menu button
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    WebDriverWait(driver, 10).until(  # Click select button in menu
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[3]'))).click()
    sleep(1)
    table_id = driver.find_element_by_xpath("//table/tbody/tr[" + str(chooseGraphicNumber) + "]/td[1]")
    choosedGraph = table_id.text
    table_id.click()
    sleep(1)
    actionChains = ActionChains(driver)
    rigthclickElement = driver.find_elements_by_class_name('badge')
    actionChains.context_click(rigthclickElement[1]).perform()
    sleep(1)
    editGraph = driver.find_element_by_xpath('//*[@id="update"]').click()
    sleep(1)
    check = driver.find_elements_by_class_name('form-control')
    print(choosedGraph)
    xBtn = driver.find_elements_by_class_name('close')
    xBtn[1].click()
    assert (choosedGraph == check[0].get_attribute('value')), 'Choose graphic failed'

def deleteGraphic (driver):
    PreviosGraphicNumber = graphicNumber(driver)
    print('PreviosGraphicNumber',PreviosGraphicNumber)
    WebDriverWait(driver, 10).until(  # Click menu button
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    WebDriverWait(driver, 10).until(  # Click select button in menu
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[3]'))).click()
    sleep(1)
    deleteButton = driver.find_element_by_xpath(
        '/html/body/div[3]/div[1]/div/div/div/form/div/div/div/table/tbody/tr[' + str(deleteGraphicNumber) + ']/td[4]/button')
    deleteButton.click()
    sleep(2)
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[2].click()
    sleep(1)
    xBtn = driver.find_elements_by_class_name('close')
    xBtn[1].click()
    sleep(2)
    CurrentGraphicNumber = graphicNumber(driver)
    print('CurrentGraphicNumber', CurrentGraphicNumber)
    assert (CurrentGraphicNumber < PreviosGraphicNumber), 'Delete graphic failed'

def editGraphic (driver):
    actionChains = ActionChains(driver)
    rigthclickElement = driver.find_elements_by_class_name('badge')
    actionChains.context_click(rigthclickElement[1]).perform()
    sleep(1)
    editGraph = driver.find_element_by_xpath('//*[@id="update"]').click()
    sleep(1)
    editTitle = driver.find_element_by_class_name('form-control')
    editTitle.clear()
    editTitle.send_keys(changeGraphicName)
    editAbout = driver.find_element_by_id('basicTextarea')
    editAbout.clear()
    editAbout.send_keys(changeGraphicAbout)
    sleep(1)
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[1].click()
    sleep(2)

def highlight (driver):
    # Done option
    WebDriverWait(driver, 10).until(  # Click menu button
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    sleep(1)
    WebDriverWait(driver, 10).until(  # Click highlight button in menu
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[1]'))).click()
    sleep(1)
    select = driver.find_element_by_id('basicSelect')
    select.click()
    for option in select.find_elements_by_tag_name('option'):
        if option.text == 'Done':  # Operation Done
            option.click()  # select() in earlier versions of webdriver
            break
    sleep(2)
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[1].click()
    sleep(2)

    # In-progress option
    WebDriverWait(driver, 10).until(  # Click menu button
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    sleep(1)
    WebDriverWait(driver, 10).until(  # Click highlight button in menu
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[1]'))).click()
    sleep(1)
    select = driver.find_element_by_id('basicSelect')
    select.click()
    for option in select.find_elements_by_tag_name('option'):
        if option.text == 'In-progress':
            option.click()  # select() in earlier versions of webdriver
            break
    sleep(2)
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[1].click()
    sleep(2)

    # Not-started option
    WebDriverWait(driver, 10).until(  # Click menu button
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    sleep(1)
    WebDriverWait(driver, 10).until(  # Click highlight button in menu
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[1]'))).click()
    sleep(1)
    select = driver.find_element_by_id('basicSelect')
    select.click()
    for option in select.find_elements_by_tag_name('option'):
        if option.text == 'Not-started':  # operation Done
            option.click()  # select() in earlier versions of webdriver
            break
    sleep(2)
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[1].click()
    sleep(2)

    # Verified option
    WebDriverWait(driver, 10).until(  # Click menu button
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    sleep(1)
    WebDriverWait(driver, 10).until(  # Click hightlight button in menu
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[1]'))).click()
    sleep(1)
    select = driver.find_element_by_id('basicSelect')
    select.click()
    for option in select.find_elements_by_tag_name('option'):
        if option.text == 'Verified':  # operation Done
            option.click()  # select() in earlier versions of webdriver
            break
    sleep(2)
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[1].click()
    sleep(1)

    # None option
    WebDriverWait(driver, 10).until(  # Click menu button
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    sleep(1)
    WebDriverWait(driver, 10).until(  # Click highlight button in menu
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[1]'))).click()
    sleep(1)
    select = driver.find_element_by_id('basicSelect')
    select.click()
    for option in select.find_elements_by_tag_name('option'):
        if option.text == 'None':
            option.click()  # select() in earlier versions of webdriver
            break
    sleep(2)
    okBtn = driver.find_elements_by_class_name('btn-primary')
    okBtn[1].click()

def searchButton (driver):
    sBtn = driver.find_element_by_class_name('vs__selected-options')
    sBtn.click()
    sleep(2)
    allText = driver.find_element_by_class_name('vs__dropdown-menu')
    searchText = allText.text
    searchText = searchText.split('\n')
    sField = driver.find_element_by_tag_name('input')
    sField.send_keys(searchText[1])
    sleep(2)
    allText = driver.find_element_by_class_name('vs__dropdown-menu')
    allText.click()
    checkElem = driver.find_element_by_class_name('bg-primary')
    # choosedText = checkElem.text
    # print(checkElem.text)
    # print(searchText[1])
    # sleep(5)
    # #assert (searchText[1] == checkElem.text), 'Search button failed'
    # sleep(1)