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
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

driver.find_element(By.ID ,'OKTab').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element(By.XPATH ,"//a[@href='#CancelTab']").click()
time.sleep(2)

driver.find_element(By.ID,'CancelTab').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element(By.XPATH ,"//a[@href='#Textbox']").click()
time.sleep(4)
driver.find_element(By.ID ,'Textbox').click()
time.sleep(2)
tx= driver.switch_to.alert.text
print(tx)
driver.switch_to.alert.send_keys("akash Bhole")
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.quit()