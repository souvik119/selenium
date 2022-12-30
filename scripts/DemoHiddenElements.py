from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoElementState():

    def demo_hidden_element(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp')
        hidden_elem_state = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(hidden_elem_state)
        time.sleep(2)
        #State is true here since element is visible

        #clicking button to hide the above element
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        time.sleep(2)

        #check the state of hidden element again
        hidden_elem_state = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(hidden_elem_state)
        #State is false here since element is hidden

    
    def demo_hidden_element_disappear(self):
        #In this case the element completely disappers from page so is_displayed will throe an exception
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.yatra.com/hotels')

        #click a few elements to get to hidden element
        driver.find_element(By.XPATH, "//label[normalize-space()='Traveller and Hotel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        time.sleep(2)
        #check state of element - should be True
        element_status = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(element_status)

        #disabling the element so it disappers from the page
        driver.find_element(By.XPATH, "//span[@class='ddSpinnerMinus disabled']").click()
        time.sleep(2)
        element_status = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(element_status)
        #this will throw NoSuchElementException since the element is no longer present on the page

find_element_obj = DemoElementState()
find_element_obj.demo_hidden_element_disappear()