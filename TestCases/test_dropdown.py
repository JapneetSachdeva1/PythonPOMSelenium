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
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Akash")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Bhole")
driver.find_element(By.XPATH,"//textarea[@class='form-control ng-pristine ng-untouched ng-valid']").send_keys("pune")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("kumar@gmail.com")
driver.find_element(By.XPATH ,"//input[@type='tel']").send_keys("9890172768")
driver.find_element(By.XPATH,"//input[@value='Male']").click()
driver.find_element(By.ID ,"checkbox1").click()
time.sleep(4)
driver.execute_script("window.scrollBy(0,500)","")
select_web=driver.find_element(By.ID , 'Skills')
sel=Select(select_web)
sel.select_by_index(5)
time.sleep(4)
sel.select_by_value("C++")
time.sleep(4)
sel.select_by_visible_text("Design")
time.sleep(2)
sel.select_by_index(2)
time.sleep(2)
sel.select_by_index(1)
time.sleep(2)
sel.select_by_visible_text("Android")
time.sleep(2)

driver.get("https://edqa.cmnetwork.co/user/login")
time.sleep(2)

driver.back()
time.sleep(2)

driver.refresh()
driver.forward()
time.sleep(4)

driver.quit()