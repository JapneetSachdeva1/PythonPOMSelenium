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
driver.get("https://www.redbus.in")
driver.implicitly_wait(2)
driver.maximize_window()


select_date = "13-08-2024"
date = select_date.split("-")

driver.find_element(By.ID ,'onwardCal').click()
td = driver.find_elements(By.XPATH,"//span[@class='DayTiles__CalendarDaysSpan-sc-14em0t0-1 fxWHuy']")

for ele in td:
    if ele.text == date[0]:
        ele.click()
        break
