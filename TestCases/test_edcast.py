
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

driver.get("https://edqa.cmnetwork.co/user/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH ,"//input[@id='email']").send_keys("aswini@edcast.com")
driver.find_element(By.XPATH ,"//input[@id='password']").send_keys("Aswini123#")
driver.find_element(By.XPATH,"//input[@id='tandc']").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()
Notification= driver.find_element(By.XPATH ,"")
Notification.click()
