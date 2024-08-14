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
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Akash")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Bhole")
driver.find_element(By.XPATH,"//textarea[@class='form-control ng-pristine ng-untouched ng-valid']").send_keys("pune")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("kumar@gmail.com")
driver.find_element(By.XPATH ,"//input[@type='tel']").send_keys("9890172768")
driver.find_element(By.XPATH,"//input[@value='Male']").click()
driver.find_element(By.ID ,"checkbox1").click()
time.sleep(4)
