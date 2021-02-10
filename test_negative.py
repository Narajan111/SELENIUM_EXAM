import pytest
from time import sleep
import re
from selenium.common.exceptions import NoSuchElementException
from locators import Locators


# @pytest.mark.skip
def test_page_validation(chrome_webdriver):
    chrome_webdriver.get('http://www.seleniumframework.com/Practiceform/')
    # print('xxxxxxxxxxxxxxxxxxxxxxx')
    # print(chrome_webdriver.title)
    assert chrome_webdriver.title == 'Selenium Framework | Practiceform'
    chrome_webdriver.quit()


# @pytest.mark.skip
def test_name_field(chrome_webdriver):
    chrome_webdriver.get("http://www.seleniumframework.com/Practiceform/")
    chrome_webdriver.find_element_by_xpath(Locators.name_xpath).send_keys("")
    chrome_webdriver.find_element_by_xpath(Locators.email_xpath).send_keys("nara@gmail.com")
    chrome_webdriver.find_element_by_xpath(Locators.phone_xpath).send_keys("88888888")

    chrome_webdriver.find_element_by_xpath(Locators.submit_btn_xpath).click()

    sleep(5)

    try:
        name_error_el=chrome_webdriver.find_element_by_xpath(Locators.name_Error_xpath)

    except NoSuchElementException:
        name_error_el = None

    finally:
        chrome_webdriver.quit()

    assert name_error_el is not None, "Name field is required"

# @pytest.mark.skip
@pytest.mark.parametrize("name, email, phone", [("Nara", "dfbfd", "88888888"), ("Nara", "", "88888888")])
def test_email_field(chrome_webdriver, name, email, phone):
    chrome_webdriver.get("http://www.seleniumframework.com/Practiceform/")
    chrome_webdriver.find_element_by_xpath(Locators.name_xpath).send_keys(name)
    chrome_webdriver.find_element_by_xpath(Locators.email_xpath).send_keys(email)
    chrome_webdriver.find_element_by_xpath(Locators.phone_xpath).send_keys(phone)
    chrome_webdriver.find_element_by_xpath(Locators.submit_btn_xpath).click()
    
    sleep(5)

    try:
        email_error_el=chrome_webdriver.find_element_by_xpath(Locators.email_Error_xpath)
        print("XXXXX")
        print(email_error_el.text)
        
    except NoSuchElementException:
        email_error_el = None

    finally:
            chrome_webdriver.quit()

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    
    if re.search(regex, email) is None:

        assert email_error_el is not None, 'Email field is required or Invalid email'
    



# @pytest.mark.skip
@pytest.mark.parametrize("name, email, phone", [("Nara", "nara@gmail.com", ""), ("Nara", "nara@gmail.com", "gge")])
def test_phone_field(chrome_webdriver, name, email, phone):
    chrome_webdriver.get("http://www.seleniumframework.com/Practiceform/")
    chrome_webdriver.find_element_by_xpath(Locators.name_xpath).send_keys(name)
    chrome_webdriver.find_element_by_xpath(Locators.email_xpath).send_keys(email)
    chrome_webdriver.find_element_by_xpath(Locators.phone_xpath).send_keys(phone)
    chrome_webdriver.find_element_by_xpath(Locators.submit_btn_xpath).click()

    sleep(5)

    try:
        phone_error_el=chrome_webdriver.find_element_by_xpath(Locators.phone_Error_xpath)
        
    except NoSuchElementException:
        phone_error_el = None
        
    finally:
            chrome_webdriver.quit()

    regex = "\w{8}"
    
    if re.search(regex, phone) is None:

        assert phone_error_el is not None, 'Phone field is required or Invalid phone number'

