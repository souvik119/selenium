from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoElementState():

    def demo_iframes(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        #have to first swtich to parent iframe to click on anything (with iframe locator)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        #swtiching to 1st child iframe
        driver.switch_to.frame(0)
        #now clicking on button
        driver.find_element(By.XPATH, "//a[@id='cert_navbtn']").click()
        time.sleep(4)


find_element_obj = DemoElementState()
find_element_obj.demo_iframes()