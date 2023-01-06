from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoElementState():

    def demo_right_double_click(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        time.sleep(2)

        #Right click
        right_click_btn = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        copy_element = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
        achains = ActionChains(driver)
        achains.context_click(right_click_btn).perform()
        time.sleep(3)
        copy_element.click()
        time.sleep(3)

        #Double click
        double_click_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        achains = ActionChains(driver)
        achains.double_click(double_click_btn).perform()
        time.sleep(3)


find_element_obj = DemoElementState()
find_element_obj.demo_right_double_click()