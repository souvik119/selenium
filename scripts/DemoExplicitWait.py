from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoElementState():

    def demo_explicit_wait(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.yatra.com/')

        #first method is to select using enter button when full keyword is typed in
        origin_city = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        origin_city.click()
        origin_city.send_keys("New Delhi")
        origin_city.send_keys(Keys.ENTER)

        #second method is to use partial keywords and work with the actual aut usggestion list
        destination_city = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        destination_city.send_keys("New")
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        for result in search_results:
            if "New York (JFK)" in result.text:
                result.click()
                break

        #implementing explicit wait here - 10s is the timeout
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        # origin_date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        # origin_date.click()

        #Implementing explicit wait
        all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "///div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))).find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        # all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "11/01/2023":
                date.click()
                break

        driver.find_element(By.XPATH, "//input[]@value='Search Flights'").click()


find_element_obj = DemoElementState()
find_element_obj.demo_explicit_wait()