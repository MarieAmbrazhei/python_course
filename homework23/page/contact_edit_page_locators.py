"""Edit contact page page"""
from selenium.webdriver.common.by import By


class EditContactPageLocators:
    """
    Class store contact edit page locators
    """

    ADD_FIRSTNAME_INPUT = (By.XPATH, '//input[@id="firstName"]')
    ADD_LASTNAME_INPUT = (By.XPATH, '//input[@id="lastName"]')
    ADD_BIRTHDATE_INPUT = (By.XPATH, '//input[@id="birthdate"]')
    ADD_EMAIL_INPUT = (By.XPATH, '//input[@id="email"]')
    ADD_PHONE_INPUT = (By.XPATH, '//input[@id="phone"]')
    ADD_STREET1_INPUT = (By.XPATH, '//input[@id="street1"]')
    ADD_STREET2_INPUT = (By.XPATH, '//input[@id="street2"]')
    ADD_CITY_INPUT = (By.XPATH, '//input[@id="city"]')
    ADD_STATE_PROVINCE_INPUT = (By.XPATH, '//input[@id="stateProvince"]')
    ADD_POSTAL_CODE_INPUT = (By.XPATH, '//input[@id="postalCode"]')
    ADD_COUNTRY_INPUT = (By.XPATH, '//input[@id="country"] ')
