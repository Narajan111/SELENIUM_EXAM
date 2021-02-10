import pytest
from time import sleep
import re
from selenium.common.exceptions import NoSuchElementException
from locators import Locators


# @pytest.mark.ok
@pytest.mark.parametrize("name, email, phone, country, company, massege", [("Nara", "nara@gmail.com", \
                        "88888888", "Armenia", "Home", "Some comments"), ("Areg", "areg@gmail.com", "5555",\
                        "USA", "", "   ")])
def test_name_field(chrome_webdriver, name, email, phone, country, company, massege):
    chrome_webdriver.get("http://www.seleniumframework.com/Practiceform/")
    chrome_webdriver.find_element_by_xpath(Locators.name_xpath).send_keys(name)
    chrome_webdriver.find_element_by_xpath(Locators.email_xpath).send_keys(email)
    chrome_webdriver.find_element_by_xpath(Locators.phone_xpath).send_keys(phone)
    chrome_webdriver.find_element_by_xpath(Locators.country_xpath).send_keys(country)
    chrome_webdriver.find_element_by_xpath(Locators.company_xpath).send_keys(company)
    chrome_webdriver.find_element_by_xpath(Locators.message_xpath).send_keys(massege)

    sleep(3)

    chrome_webdriver.find_element_by_xpath(Locators.submit_btn_xpath).click()
    
    sleep(2)

    try:
        accept_notif=chrome_webdriver.find_element_by_xpath(Locators.accept_xpath)

    except NoSuchElementException:
        accept_notif=None
        
    finally:
        chrome_webdriver.quit()

    assert accept_notif is not None, "Something is wrong :)"

