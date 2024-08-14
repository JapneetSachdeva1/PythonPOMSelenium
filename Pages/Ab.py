from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
#driver.find_element(By.NAME,"name").send_keys("Kumar")
#driver.find_element(By.ID,"name").send_keys("Kumar")
#driver.find_element_by_id("name").send_keys("Ramesh")
#driver.find_element(By.CLASS_NAME,"nor-text").send_keys("ffhfdsjbfshfd")
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Akash")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Bhole")
driver.find_element(By.XPATH,"//textarea[@class='form-control ng-pristine ng-untouched ng-valid']").send_keys("pune")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("kumar@gmail.com")
driver.find_element(By.XPATH ,"//input[@type='tel']").send_keys("9890172768")
driver.find_element(By.XPATH,"//input[@value='Male']").click()
driver.find_element(By.ID ,"checkbox1").click()
select = driver.find_element(By.XPATH,"//div[@id='msdd']").click()
select.select_by_value("Arabic")
time.sleep(4)
driver.close()