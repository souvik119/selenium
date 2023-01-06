from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoElementState():

    def demo_drag_drop(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(2)

        #first swtiching to iframe
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

        drag_element = driver.find_element(By.ID, "draggable")
        drop_element = driver.find_element(By.ID, "droppable")

        #1st method
        ActionChains(driver).drag_and_drop(drag_element, drop_element).perform()
        time.sleep(4)

        #2nd method here offset is not the actual x and y coordinates but offset from the drag element
        ActionChains(driver).drag_and_drop_by_offset(drag_element, 100, 100).perform()
        time.sleep(4)

find_element_obj = DemoElementState()
find_element_obj.demo_drag_drop()