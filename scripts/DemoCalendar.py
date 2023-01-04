from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class DemoElementState():

    def demo_calendar(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.yatra.com/')
        time.sleep(2)

        #first method is to select using enter button when full keyword is typed in
        origin_date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin_date.click()
        time.sleep(2)
        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "11/01/2023":
                date.click()
                time.sleep(4)
                break
                

find_element_obj = DemoElementState()
find_element_obj.demo_calendar()