from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoElementState():

    def demo_multiple_windows(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(2)

        #getting current window handle
        parent_handle = driver.current_window_handle
        print(parent_handle)

        driver.find_element(By.XPATH, "//a[normalize-space()='View All']").click()
        time.sleep(2)

        all_page_handles = driver.window_handles
        print(all_page_handles)
        for handle in all_page_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                print(driver.find_element(By.XPATH, "//p[normalize-space()='Coupon Code : YTICICIEMI']").text)
                time.sleep(4)
                driver.close()
                time.sleep(2)
                break

        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//a[@title='Round Trip']").click()
        time.sleep(4)
                

find_element_obj = DemoElementState()
find_element_obj.demo_multiple_windows()