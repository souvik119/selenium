from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DemoElementState():

    def demo_dropdown(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.seleniumeasy.com/basic-select-dropdown-demo.html')
        time.sleep(2)

        #this method only works with dropdows implemented via select tag
        dd_demo = driver.find_element(By.ID, "multi-select")
        dd_multi = Select(dd_demo)

        #three ways of selcting options
        dd_multi.select_by_index(0)
        dd_multi.select_by_visible_text("Florida")
        dd_multi.select_by_value("New Jersey")
        dd_multi.select_by_index(3)
        dd_multi.select_by_visible_text("Texas")
        dd_multi.select_by_value("Ohio")
        time.sleep(2)

        dd_multi.deselect_by_index(0)
        dd_multi.deselect_by_value("New Jersey")
        dd_multi.deselect_by_visible_text("Florida")
        time.sleep(2)

        dd_multi.deselect_all()
        time.sleep(2)


find_element_obj = DemoElementState()
find_element_obj.demo_dropdown()