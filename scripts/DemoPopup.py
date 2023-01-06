from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoElementState():

    def demo_popup(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        time.sleep(2)
        #switch to iframe first since button for popup is inside the iframe
        driver.switch_to.frame("iframeResult")

        #accept the alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        #handling js alerts now
        driver.switch_to.alert.accept()
        time.sleep(2)
        
        #dismiss the alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        #handling js alerts now
        driver.switch_to.alert.dismiss()
        time.sleep(2)

        #send keys to alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        #handling js alerts now
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys("Test User")
        driver.switch_to.alert.accept()
        time.sleep(2)


find_element_obj = DemoElementState()
find_element_obj.demo_popup()