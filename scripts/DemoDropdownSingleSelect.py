from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DemoElementState():

    def demo_dropdown(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.salesforce.com/form/demo/salesforce-products/?gclid=EAIaIQobChMInYfT3sGi_AIVbw6tBh3T8A8fEAAYASAAEgIGLPD_BwE&d=7010M000001ynfX&nc=7010M000002QR17&DCMP=KNC-Google&ef_id=EAIaIQobChMInYfT3sGi_AIVbw6tBh3T8A8fEAAYASAAEgIGLPD_BwE:G:s&s_kwcid=AL!4604!3!519117946766!e!!g!!salesforce&gclsrc=aw.ds')
        time.sleep(2)

        #this method only works with dropdows implemented via select tag
        country_dd = driver.find_element(By.NAME, "CompanyCountry")
        dd = Select(country_dd)

        #three ways of selcting options
        dd.select_by_index(10)
        time.sleep(2)

        dd.select_by_visible_text("India")
        time.sleep(2)

        dd.select_by_value("US")
        time.sleep(2)


find_element_obj = DemoElementState()
find_element_obj.demo_dropdown()