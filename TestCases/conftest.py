from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager

from Utilities import ConfigReader


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def get_browser(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#    print(ConfigReader.readConfig("base_url", "testsiteurl"))
  #  driver.get(ConfigReader.readConfig("base_url", "testsiteurl"))
    driver.get("https://way2automation.com/way2auto_jquery/index.php")
    driver.maximize_window()
    yield driver
    driver.quit()
