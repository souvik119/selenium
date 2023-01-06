from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoElementState():

    def demo_slider(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=e7624080-b2a4-4437-8a0f-fa4b35807328")
        time.sleep(2)

        left_slider = driver.find_element(By.XPATH, "//div[@class='_31Kbhn _28DFQy']")
        right_slider = driver.find_element(By.XPATH, "//div[@class='_31Kbhn WC_zGJ']")

        # drag left slider to the right by 60 pixels
        ActionChains(driver).drag_and_drop_by_offset(left_slider, 60, 0).perform()
        time.sleep(3)

        # 2nd method if above does not work
        ActionChains(driver).click_and_hold(left_slider).pause(1).move_by_offset(60, 0).release().perform()

        #3rd method
        ActionChains(driver).move_to_element(left_slider).pause(1).click_and_hold(left_slider).move_by_offset(60, 0).release().perform()

        #move right slider to the left by 60 pixels
        ActionChains(driver).drag_and_drop_by_offset(right_slider, -60, 0).perform()
        time.sleep(3)       


find_element_obj = DemoElementState()
find_element_obj.demo_slider()