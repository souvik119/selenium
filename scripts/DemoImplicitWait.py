from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoElementState():

    def demo_implcit_wait(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #implicit wait is for the whole session and not for individual elements and it is dynamic
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/")
        #using wrong ID here just to make sure driver waits
        driver.find_element(By.ID, "username12").send_keys("Test")
         


find_element_obj = DemoElementState()
find_element_obj.demo_implcit_wait()