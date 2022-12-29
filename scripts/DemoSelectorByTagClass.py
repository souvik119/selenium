from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoFindElement():

    def locate_by_tag(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element(By.TAG_NAME, 'input').send_keys('test@test.com')
        time.sleep(4)


    def locate_by_class(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        #before copying from selectors hub make sure class name has no space, space means multiple classes
        driver.find_element(By.CLASS_NAME, 'email-login-box').send_keys('test@test.com')
        time.sleep(4)

find_element_obj = DemoFindElement()
find_element_obj.locate_by_class()