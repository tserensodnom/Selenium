from time import sleep
from utils.functions import engine, edit


def graphicNumber(driver):
    table = driver.find_element_by_tag_name('table')
    sum = table.get_attribute('aria-rowcount')  # TODO aria-rowcountF Shalgah
    print(sum)
    return sum


def createGraphic(driver, data):
    pre = graphicNumber(driver)
    engine(driver, data)
    cur = graphicNumber(driver)
    # assert (pre < cur), 'Create graphic failed'


def chooseGraphic(driver, data):
    engine(driver, data)
    # driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div[1]/div/div[1]/button/button').click()
    # el = driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div[1]/div/div[1]/ul/div/div/div[2]/section[1]/form/div/div/div/table/tbody/tr[2]')
    # el.click()
    sleep(1)
    # WebDriverWait(driver, 10).until(  # Click menu button
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-wrapper"]'))).click()
    # WebDriverWait(driver, 10).until(  # Click select button in menu
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="bottom-right-action"]/ul/li[3]'))).click()
    # sleep(1)
    # table_id = driver.find_element_by_xpath("//table/tbody/tr[" + str(chooseGraphicNumber) + "]/td[1]")
    # choosedGraph = table_id.text
    # table_id.click()
    # sleep(1)
    # actionChains = ActionChains(driver)
    # rigthclickElement = driver.find_elements_by_class_name('badge')
    # actionChains.context_click(rigthclickElement[1]).perform()
    # sleep(1)
    # editGraph = driver.find_element_by_xpath('//*[@id="update"]').click()
    # sleep(1)
    # check = driver.find_elements_by_class_name('form-control')
    # print(choosedGraph)
    # xBtn = driver.find_elements_by_class_name('close')
    # xBtn[1].click()
    # assert (choosedGraph == check[0].get_attribute('value')), 'Choose graphic failed'


def deleteGraphic(driver, data):
    pre = graphicNumber(driver)
    engine(driver, data)
    cur = graphicNumber(driver)
    # assert (pre > cur), 'Delete graphic failed'


def editGraphic(driver, data):
    edit(driver, x='edit', i=0)
    engine(driver, data)
    edit(driver, x='edit', i=0)
    nameCheck = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/form/div[1]/div/input')
    aboutCheck = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/form/div[3]/div/textarea')
    sleep(1)
    xbtn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/button[1]')
    xbtn.click()
    assert (nameCheck.get_attribute('value') == data[0]['value'] and
            aboutCheck.get_attribute('value') == data[1]['value']), 'Failed edit graphic'


def highlight(driver, data):
    for elem in data[0]['value']:
        clickBtn = driver.find_element_by_xpath(
            '/html/body/div/div/div/div/main/div/div/div[1]/div/div[2]/div/div[2]/button/button')
        clickBtn.click()
        sleep(1)
        select = driver.find_element_by_id('basicSelect')
        select.click()
        sleep(1)
        for option in select.find_elements_by_tag_name('option'):
            if option.text == elem:  # Operation Done
                option.click()  # select() in earlier versions of webdriver
                sleep(1)
                break
        sleep(1)


def searchButton(driver, data):
    engine(driver, data)
    allText = driver.find_element_by_class_name('vs__dropdown-menu')
    searchText = allText.text
    searchText = searchText.split('\n')
    searchText = searchText[0].split(' ')
    sField = driver.find_element_by_xpath(
        '/html/body/div/div/div/div/main/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/input')
    sField.send_keys(searchText[0])
    allText = driver.find_element_by_class_name('vs__dropdown-menu')
    allText.click()
    checkElem = driver.find_element_by_class_name('bg-primary')
    assert (checkElem.value_of_css_property('background-color') == 'rgba(32, 168, 216, 1)'), 'Search button failed'
