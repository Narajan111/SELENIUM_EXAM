class Locators:
    name_xpath = "//input[@name='name']" 

    email_xpath = "//span[@class='form-mail']/input"

    phone_xpath = "//span[@class='form-telephone']/input"

    country_xpath = "//input[@name='country']"

    company_xpath = "//input[@name='company']"

    message_xpath = "//textarea[@name='message']"

    submit_btn_xpath = "//a[@class='dt-btn dt-btn-m dt-btn-submit']"

    clear_btn_xpath = "//a[@class='clear-form']"


    name_Error_xpath = "//div[@id='page']/div[@id='main']/div[2]/div[1]/aside[1]/div[1]/section[2]/form[1]/div[1]/span[1]/div[1]/div[1]" 

    email_Error_xpath = "//div[@id='page']/div[@id='main']/div[2]/div[1]/aside[1]/div[1]/section[2]/form[1]/div[1]/span[2]/div[1]/div[1]"

    phone_Error_xpath = "//div[@id='page']/div[@id='main']/div[2]/div[1]/aside[1]/div[1]/section[2]/form[1]/div[1]/span[3]/div[1]/div[1]"


    accept_xpath = "//div[contains(text(),'Feedback has been sent to the administrator')]"
