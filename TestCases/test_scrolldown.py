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

time.sleep(4)
driver.execute_script("window.scrollBy(0,1000)","")
driver.close()