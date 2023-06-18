from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities import ConfigReader


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # helps to fill registration form
    def register_user(self, name, phone, email, city, username, password):
        self.typeText("locators_RegistrationPage", "name_XPATH", name)
        self.typeText("locators_RegistrationPage", "phone_XPATH", phone)
        self.typeText("locators_RegistrationPage", "email_XPATH", email)
        # country dropDown
        self.select("locators_RegistrationPage", "dropDown_XPATH", "Germany")
        self.typeText("locators_RegistrationPage", "city_XPATH", city)
        self.typeText("locators_RegistrationPage", "username_XPATH", username)
        self.typeText("locators_RegistrationPage", "password_XPATH", password)
        self.performClick("locators_RegistrationPage","submit_XPATH")

