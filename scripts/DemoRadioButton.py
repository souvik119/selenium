from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoElementState():

    def demo_radio_button(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.sugarcrm.com/au/request-demo/')
        time.sleep(2)

        #check state of buttons before anything is clicked
        print(driver.find_element(By.ID, "doi0").is_selected())
        print(driver.find_element(By.ID, "doi1").is_selected())

        #click on first radio button
        driver.find_element(By.ID, "doi0").click()
        time.sleep(2)

        #check state of buttons after first radio button is clicked
        print(driver.find_element(By.ID, "doi0").is_selected())
        print(driver.find_element(By.ID, "doi1").is_selected())

        #click on second radio button
        driver.find_element(By.ID, "doi1").click()
        time.sleep(2)

        #check state of buttons after second radio button is clicked
        print(driver.find_element(By.ID, "doi0").is_selected())
        print(driver.find_element(By.ID, "doi1").is_selected())



find_element_obj = DemoElementState()
find_element_obj.demo_radio_button()