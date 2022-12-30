from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoElementState():

    def demo_checkbox(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.yatra.com/')
        #click to check the box
        driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").click()
        time.sleep(2)
        #verify that box was checked
        checkbox_state = driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").is_selected()
        print(checkbox_state)

        #repeating the same for another checkbox
        driver.find_element(By.XPATH, "//a[normalize-space()='Student Fare']").click()
        time.sleep(2)
        checkbox_state1 = driver.find_element(By.XPATH, "//a[normalize-space()='Student Fare']").is_selected()
        print(checkbox_state1)

        #not selecting a box and making sure is_selected state is False
        checkbox_state2 = driver.find_element(By.XPATH, "//a[normalize-space()='Armed Forces']").is_selected()
        print(checkbox_state2)


find_element_obj = DemoElementState()
find_element_obj.demo_checkbox()