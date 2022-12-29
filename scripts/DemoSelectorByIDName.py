from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "./drivers/chromedriver.exe"

class DemoFindElementByIDName():

    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element(By.ID, 'login-input').send_keys('test@test.com')
        time.sleep(4)

    def locate_by_name_demo(self):
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element(By.NAME, 'login-input').send_keys('test@test.com')
        time.sleep(4)


findbyname = DemoFindElementByIDName()
findbyname.locate_by_name_demo()