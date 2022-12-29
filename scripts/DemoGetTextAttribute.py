from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoFindElement():

    def find_text(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.yatra.com/')
        found_text = driver.find_element(By.XPATH, "//p[contains(text(),'On Yatra.com, you can tailor your trip from end-to')]").text
        print(found_text)
        time.sleep(4)


    def find_attribute(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.yatra.com/')
        #before copying from selectors hub make sure class name has no space, space means multiple classes
        found_attribute = driver.find_element(By.XPATH, "//div[normalize-space()='Dubai']").get_attribute("class")
        print(found_attribute)
        time.sleep(4)

find_element_obj = DemoFindElement()
find_element_obj.find_text()
find_element_obj.find_attribute()