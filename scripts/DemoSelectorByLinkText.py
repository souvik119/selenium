from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


class DemoFindElement():

    def locate_by_id_link_text(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #using link text here and not href
        driver.get('https://www.yatra.com/')
        element = driver.find_element(By.LINK_TEXT, 'Yatra for Business')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(4)


    def locate_by_id_partial_link_text(self):
        #if only part of link text is static other part is dynamically generated
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.yatra.com/')
        element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Yatra for')
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(4)

find_element_obj = DemoFindElement()
find_element_obj.locate_by_id_link_text()