from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class DemoElementState():

    def demo_autoselect(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.yatra.com/')
        time.sleep(2)

        #first method is to select using enter button when full keyword is typed in
        origin_city = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        origin_city.click()
        time.sleep(2)
        origin_city.send_keys("New Delhi")
        time.sleep(2)
        origin_city.send_keys(Keys.ENTER)
        time.sleep(4)

        #second method is to use partial keywords and work with the actual aut usggestion list
        destination_city = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        destination_city.send_keys("New")
        time.sleep(2)
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        for result in search_results:
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(4)
                break


find_element_obj = DemoElementState()
find_element_obj.demo_autoselect()