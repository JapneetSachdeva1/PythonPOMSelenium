from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from asyncio.tasks import wait
# Basic code 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Windows.html")
driver.implicitly_wait(2)
driver.maximize_window()
# Navigate to windows 

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("akashbhole231@gmail.com")
driver.find_element(By.XPATH ,"//button[@id='btn2']").click()
driver.implicitly_wait(2)

wait=webdriver.wait(driver , 5)
wait.until(EC.visibility_of_located_element(driver.find_element(By.XPATH ,"//a[@href='SwitchTo.html']").click()))



