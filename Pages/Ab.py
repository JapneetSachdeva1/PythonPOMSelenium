import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(5)
driver.find_element("name","q").send_keys("LinkedinLogin")
driver.find_element("name","q").send_keys(Keys.ENTER)
time.sleep(3)
button_L=driver.find_element(by=By.LINK_TEXT,value = "Login")
button_L.click()
time.sleep(5)