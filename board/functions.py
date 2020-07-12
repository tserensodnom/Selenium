from time import sleep
from selenium.webdriver import ActionChains
from utils.functions import engine


def drag(driver, data):
    engine(driver, data)
    driver.refresh()
    source = driver.find_elements_by_class_name('mb-0')
    target = driver.find_elements_by_class_name('drag-inner-list')
    for idx, elem in enumerate(source):
        if idx == 0:
            continue
        else:
            sleep(1)
            ActionChains(driver).drag_and_drop(source[idx], target[idx]).perform()
            sleep(1)
    # elem = driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div[3]/ul/li[1]/ul/li[1]/div')
    # target = driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div[3]/ul/li[2]/ul')
    # ActionChains(driver).drag_and_drop(elem, target).perform()
    sleep(1)
