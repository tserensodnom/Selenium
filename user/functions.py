from time import sleep
import json

username = 'test0'
password = '1234567'
email = 'tserensodnom.t@gmail.com'
firstname = 'firstName'
lastname = 'lastName'
usernameChange = 'test0'
emailChange = 'tserensodnom.tt@gmail.com'
firstnameChange = 'firstnameChange'
lastnameChange = 'lastnameChange'
avatarChange = '/home/tserensodnom/Pictures/download (1).png'
newPassword = '123456789'

def createAccount(driver): #TODO xpath iig yalgah
    with open(r'/home/tserensodnom/Desktop/Uulzal project/Code project1/user/config.json') as f:
        data = json.load(f)
    for state in data['create']:
        print(state['value'])
        sleep(1)
        if state['clickable'] == True:
            elem = driver.find_element_by_xpath(state['xpath'])
            elem.click()
            sleep(1)
        else:
            elem = driver.find_element_by_xpath(state['xpath'])
            elem.send_keys(state['value'])
    login = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/main/div/div/div[1]/div/strong')
    assert(login.text == 'Login'), 'Create account failed'

def logIn(driver):
    enterUsername = driver.find_element_by_css_selector('#__BVID__10')
    enterUsername.send_keys(username)
    enterPassword = driver.find_element_by_xpath('//*[@id="__BVID__12"]')
    enterPassword.send_keys(str(password))
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/main/div/div/div[2]/form/div[3]/button[2]').click()
    sleep(2)
    url = driver.current_url
    assert (url == 'http://www.uulzalt.com:8001/#/mindmap'
            or url == 'http://www.uulzalt.com:8001/?#/mindmap'
            or url == 'http://www.uulzalt.com:8001/#/login'),'Login failed'

def logOut(driver):
    # userBtn = driver.find_elements_by_class_name('nav-item') # Click profile setting icon
    # userBtn[0].click()
    # sleep(1)
    # driver.find_element_by_link_text('Logout').click()  # Click Logout
    # sleep(2)
    with open(r'/home/tserensodnom/Desktop/Uulzal project/Code project1/user/config.json') as f:
        data = json.load(f)
    for state in data['logout']:
        if state['first'] == True:
            elem = driver.find_elements_by_class_name(state['method'])
            print(state['method'])
            elem[0].click()
            sleep(1)
        else:
            elem = driver.\
                find_element_by_link_text(state['method'])
            elem.click()
            sleep(2)
    url = driver.current_url
    assert (url == 'http://www.uulzalt.com:8001/#/login' or url == 'http://www.uulzalt.com:8001/?#/login' ), 'Logout failed'

def basicInfo(driver):
    imageIcon = driver.find_element_by_class_name('nav-link')
    imageIcon.click()
    sleep(2)
    accountSetting = driver.find_element_by_link_text('Account Settings')
    accountSetting.click()
    info = driver.find_elements_by_tag_name('input')
    info[0].clear() #TODO loop
    info[0].send_keys(usernameChange)
    info[1].clear()
    info[1].send_keys(emailChange)
    info[2].clear()
    info[2].send_keys(firstnameChange)
    info[3].clear()
    info[3].send_keys(lastnameChange)
    info[4].clear()
    info[4].send_keys(avatarChange)
    # browse = driver.find_element_by_class_name('custom-file-label')
    # driver.execute_script("arguments[0].click();", browse)
    submit = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/main/div/div[1]/div[2]/form/div[6]/button')
    submit.click()
    sleep(2)
    #driver.get(driver.current_url)
    info = driver.find_elements_by_class_name('form-control')
    assert (usernameChange == info[0].get_attribute('value')), 'Basic info change failed'
    assert (emailChange == info[1].get_attribute('value')), 'Basic info change failed'
    assert (firstnameChange == info[2].get_attribute('value')), 'Basic info change failed'
    assert (lastnameChange == info[3].get_attribute('value')), 'Basic info change failed'
    assert (info[4].get_attribute('value') == ''), 'Basic info change failed'

def changePassword(driver):
    info = driver.find_elements_by_tag_name('input')
    info[5].send_keys(password)
    info[6].send_keys(newPassword)
    info[7].send_keys(newPassword)
    changeBtn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/main/div/div[2]/div[2]/form/div[4]/button')
    changeBtn.click()
    sleep(2)
    check = driver.find_element_by_class_name('text-success')
    assert (check.text == 'Password has changed'), 'Password change failed'

# TODO engine version 1
# sequence = [
#     {
#         "xpath":"",
#         "clickable": True
#     },
#     {
#         "xpath":"",
#         "clickable": False,
#         "value": "asf"
#     }
# ]
#
# def engine(driver, sequence):
#     for elem in sequence:
#         element = driver.find_element_by_xpath(elem["xpath"])
#         if elem["clickable"]:
#             element.click()
#         else:
#             element.send_keys(elem["value"])

#
def engine(driver, sequence):
    sequence[0]["findElement"]["value"]