from time import sleep
from utils.functions import engine


def createAccount(driver, data):  # TODO xpath iig yalgah
    engine(driver, data)
    # checkElem = driver.find_element_by_xpath('/html/body/div/form/div[2]/div')
    # print(checkElem.text)
    # assert (checkElem.text == '❗ Таны оруулсан э-мэйл хаяг бүртгэлтэй байна.'), 'Create account failed'


def logIn(driver, data):
    engine(driver, data)
    url = driver.current_url
    assert (url == 'https://mindtask.app/#/mindmap'), 'Login failed'
    sleep(1)


def logOut(driver, data):
    engine(driver, data)
    url = driver.current_url
    assert (url == 'https://auth.bolor.net/login?t=MindTask'), 'Logout failed'


def basicInfo(driver, data):
    engine(driver, data)
    sleep(1)
    info = driver.find_elements_by_class_name('form-control')
    for idx, elem in enumerate(info):
        if idx < 4:
            assert (elem.get_attribute('value') == data[idx + 1]['value']), 'Basic info change failed'
        elif idx == 4:
            assert (elem.get_attribute('value') == ''), 'Basic info change failed'
            break


def changePassword(driver, data):
    engine(driver, data)
    check = driver.find_element_by_class_name('text-success')
    assert (check.text == 'Password has changed'), 'Password change failed'


def createCompany(driver, data):
    pre = driver.find_elements_by_class_name('button')
    engine(driver, data)
    cur = driver.find_elements_by_class_name('button')
    assert (pre < cur), 'Create company failed'


def backHomepage(driver, data):
    engine(driver, data)
