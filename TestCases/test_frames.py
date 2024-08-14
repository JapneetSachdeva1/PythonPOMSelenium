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
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
time.sleep(2)


#frame1 = driver.find_element(By.XPATH ,"//a[normalize-space()='Single Iframe']")
#driver.switch_to.frame(frame1)

frame2 = driver.find_element(By.TAG_NAME,"input")
driver.switch_to(frame2)

time.sleep(2)

driver.switch_to.default_content()
