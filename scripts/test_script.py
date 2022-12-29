from selenium import webdriver

chrome_driver_path = "./drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.google.com")
driver.maximize_window()
print(driver.title)
driver.close()