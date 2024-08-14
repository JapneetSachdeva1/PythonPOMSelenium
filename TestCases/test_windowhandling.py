from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
# Basic code 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
# Navigate to windows 
'''
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("akashbhole231@gmail.com")
driver.find_element(By.XPATH ,"//button[@id='btn2']").click()
web_sel= driver.find_element(By.XPATH ,"//a[@href='SwitchTo.html']")
sel = web_sel.click()
time.sleep(2)
driver.find_element(By.XPATH , "//a[@href='Windows.html']").click()
'''
#Navigate to windows handles 
parent =driver.current_window_handle
print(parent)
driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']").click()
windows =driver.window_handles
for win in windows:
    if win != parent :
        driver.switch_to.window(win)

driver.find_element(By.XPATH , "//a[@href='/documentation']").click()
driver.switch_to.window(parent)

driver.close()
