import pytest
from selenium import webdriver

@pytest.fixture
def chrome_webdriver():

    PATH = 'drivers/chromedriver.exe'

    driver=webdriver.Chrome(PATH)

    driver.maximize_window()

    return driver