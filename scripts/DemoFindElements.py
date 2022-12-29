from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoFindElement():

    def find_elements(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.yatra.com/')
        link_list = driver.find_elements(By.TAG_NAME, 'a')
        print(f'Number of links on the page are : {len(link_list)}')
        for link in link_list:
            print(link.text)
        time.sleep(4)

find_element_obj = DemoFindElement()
find_element_obj.find_elements()