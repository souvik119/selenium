from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoElementState():

    def demo_enable_disable(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://training.openspan.com/login')
        #Sign In button is disabled when username and passsword are blank
        button_state = driver.find_element(By.CSS_SELECTOR, "#login_button").is_enabled()
        print(button_state)

        time.sleep(2)

        #checking if Sign In button is enabled when username and passsword are filled in
        driver.find_element(By.CSS_SELECTOR, "#user_name").send_keys("testing")
        driver.find_element(By.CSS_SELECTOR, "#user_pass").send_keys("testing123")
        time.sleep(2)
        button_state = driver.find_element(By.CSS_SELECTOR, "#login_button").is_enabled()
        print(button_state)

find_element_obj = DemoElementState()
find_element_obj.demo_enable_disable()