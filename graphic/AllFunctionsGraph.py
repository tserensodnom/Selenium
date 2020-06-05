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

def logIn(driver, password):
    enter_username = driver.find_element_by_css_selector('#__BVID__10')
    enter_username.send_keys('test0')
    enter_password = driver.find_element_by_xpath('//*[@id="__BVID__12"]')
    enter_password.send_keys(str(password))
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/main/div/div/div[2]/form/div[3]/button[2]').click()
    sleep(2)

def createGraphic (driver):
    WebDriverWait(driver, 10).until(  # Click menu button
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    WebDriverWait(driver, 10).until(  # Click select button in menu
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[3]'))).click()
    sleep(1)
    a = driver.find_elements_by_class_name('page-link')

    for i in range(len(a) - 2):
        print(i)
        previousGraphics = driver.find_elements_by_tag_name('tr')
        print(len(previousGraphics))
        if i == (len(a) - 3) :
            break
        else:
            print('a:',len(a))
            a[len(a) - 1].click()
    sleep(1)
    xBtn = driver.find_elements_by_class_name('close')
    xBtn[1].click()
    sleep(1)
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
    WebDriverWait(driver, 10).until(  # Click menu button
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    WebDriverWait(driver, 10).until(  # Click select button in menu
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[3]'))).click()
    sleep(1)
    currentGraphics = driver.find_elements_by_tag_name('tr')
    print(len(currentGraphics))
    xBtn = driver.find_elements_by_class_name('close')
    xBtn[1].click()

def chooseGraphic (driver):
    WebDriverWait(driver, 10).until(  # Click menu button
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    WebDriverWait(driver, 10).until(  # Click select button in menu
        EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[3]'))).click()
    sleep(1)
    table_id = driver.find_element_by_xpath("//table/tbody/tr[" + str(chooseGraphicNumber) + "]/td[1]")
    table_id.click()
    sleep(2)

def deleteGraphic (driver):
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
