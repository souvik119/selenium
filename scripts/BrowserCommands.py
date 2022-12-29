from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# driver.get() - Navigate to a particular URL, it is a method
# driver.current_url - Read URL from browser's address bar, it is a property
# driver.back() - back button, method
# driver.forward() - forward button, method
# driver.refresh() - refresh button, method
# driver.title - get page title, property
# driver.maximize_window() - full screen, method
# driver.minimize_window() - minimize window, method
# driver.fullscreen_window() - fills entire screen similar to F11, method
# driver.close() - closes current window, method
# driver.quit() - closes all windows and tabs associated with the current session, method

class DemoBrowserMethods():

    def demo_open_browser(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://training.rcvacademy.com')
        time.sleep(4)

    def demo_get_url_title(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://training.rcvacademy.com')
        print(driver.current_url)
        print(driver.title)
        time.sleep(4)

    def demo_resize_window(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://training.rcvacademy.com')
        driver.maximize_window()
        time.sleep(2)
        driver.fullscreen_window()
        time.sleep(2)
        driver.minimize_window()
        time.sleep(2)

    def demo_forward_back_refresh(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://training.rcvacademy.com')
        time.sleep(2)       
        driver.find_element(By.LINK_TEXT, 'ALL COURSES').click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)



new_browser = DemoBrowserMethods()
new_browser.demo_forward_back_refresh()