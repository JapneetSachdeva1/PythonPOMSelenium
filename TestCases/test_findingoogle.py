from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME,"q")
searchbox.send_keys("linkedinlogin")
searchbox.submit()
driver.implicitly_wait(5)

target = driver.find_element(By.XPATH ,"//a[normalize-space()='Login']")
print(target.text)
target.click()
time.sleep(5)
