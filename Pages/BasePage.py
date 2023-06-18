from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities import ConfigReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def performClick(self, page_name, locator):
        self.driver.find_element(By.XPATH, ConfigReader.readConfig(page_name, locator)).click()

    def typeText(self, page_name, locator, text):
        self.driver.find_element(By.XPATH, ConfigReader.readConfig(page_name, locator)).send_keys(text)
        #print(page_name, locator, text)

    def select(self, page_name, locator, value):
        dropDown = self.driver.find_element(By.XPATH, ConfigReader.readConfig(page_name, locator))
        select = Select(dropDown)
        select.select_by_visible_text(value)
