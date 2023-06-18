from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read("../TestData/config.ini")
    return config.get(section, key)

print("locators_RegistrationPage", "name_XPATH")
