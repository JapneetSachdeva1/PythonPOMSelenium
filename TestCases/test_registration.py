import pytest

from Pages.RegistrationPage import RegistrationPage
from Utilities.read_csv_data import read_test_data_from_csv
from TestCases.conftest import get_browser


class Test_RegistrationPage:

    @pytest.mark.parametrize("name, phone, email, city, username, password", read_test_data_from_csv())
    def test_registration(self, name, phone, email, city, username, password, get_browser):
        self.driver = get_browser  # trigger chrome browser
        registration_page = RegistrationPage(self.driver)
        print(password)
        registration_page.register_user(name, phone, email, city, username, password)
        # print all the logs
        print("Name: "+name)
        print("phone: "+phone)
        print("email: "+email)
        print("city: "+city)
        print("username: "+username)
        print("password: "+password)
