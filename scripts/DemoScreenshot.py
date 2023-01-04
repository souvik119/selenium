from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoElementState():

    def demo_screenshot(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        time.sleep(2)

        continue_button = driver.find_element(By.ID, "login-continue-btn")
        continue_button.screenshot(".\\button.png")
        #screenshot of only the element
        continue_button.click()
        time.sleep(2)
        #screenshot of the whole screen
        driver.get_screenshot_as_file(".\\file_screenshot.png")
        driver.save_screenshot(".\\save_screenshot.png")
                

find_element_obj = DemoElementState()
find_element_obj.demo_screenshot()