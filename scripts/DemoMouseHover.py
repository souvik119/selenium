from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoElementState():

    def demo_mouse_hover(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(2)
        #action chains class can control low level interactions like mouse movement and so on
        more_btn = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        achains = ActionChains(driver)
        achains.move_to_element(more_btn).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
        time.sleep(4)

find_element_obj = DemoElementState()
find_element_obj.demo_mouse_hover()