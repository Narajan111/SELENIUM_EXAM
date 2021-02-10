import pytest
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from locators import Locators


# @pytest.mark.clear_btn
@pytest.mark.parametrize("name, email, phone, country, company, massege", [("Nara", "dfbfd", "88888888", "Armenia",\
                         "Home", "Some comments"), ("Areg", "areg@gmail.com", "", "", "aaa", "Hello")])
def test_name_field(chrome_webdriver, name, email, phone, country, company, massege):
    chrome_webdriver.get("http://www.seleniumframework.com/Practiceform/")
    chrome_webdriver.find_element_by_xpath(Locators.name_xpath).send_keys(name)
    chrome_webdriver.find_element_by_xpath(Locators.email_xpath).send_keys(email)
    chrome_webdriver.find_element_by_xpath(Locators.phone_xpath).send_keys(phone)
    chrome_webdriver.find_element_by_xpath(Locators.country_xpath).send_keys(country)
    chrome_webdriver.find_element_by_xpath(Locators.company_xpath).send_keys(company)
    chrome_webdriver.find_element_by_xpath(Locators.message_xpath).send_keys(massege)

    sleep(3)

    chrome_webdriver.find_element_by_xpath(Locators.clear_btn_xpath).click()
    
    sleep(1)

    some_string=chrome_webdriver.find_element_by_xpath(Locators.name_xpath).text+\
    chrome_webdriver.find_element_by_xpath(Locators.email_xpath).text+\
    chrome_webdriver.find_element_by_xpath(Locators.phone_xpath).text+\
    chrome_webdriver.find_element_by_xpath(Locators.country_xpath).text+\
    chrome_webdriver.find_element_by_xpath(Locators.company_xpath).text+\
    chrome_webdriver.find_element_by_xpath(Locators.message_xpath).text
  
    assert len(some_string)==0, "There is a not empty field"

    chrome_webdriver.quit()