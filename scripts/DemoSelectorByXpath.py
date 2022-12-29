from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "./drivers/chromedriver.exe"

class DemoFindElement():

    def locate_by_id_xpath(self):
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        #using relative xpath here
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys('test@test.com')
        time.sleep(4)


find_element_obj = DemoFindElement()
find_element_obj.locate_by_id_xpath()