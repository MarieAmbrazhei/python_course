from selenium.webdriver.common.by import By

"""Add contact page page"""


class AddContactPageLocators:
    """
    Class store add contact page locators
    """
    ADD_FIRSTNAME_INPUT = (By.CSS_SELECTOR, '#firstName')
    ADD_LASTNAME_INPUT = (By.CSS_SELECTOR, '#lastName')
    ADD_BIRTHDATE_INPUT = (By.CSS_SELECTOR, '#birthdate')
    ADD_EMAIL_INPUT = (By.CSS_SELECTOR, '#email')
    ADD_PHONE_INPUT = (By.CSS_SELECTOR, '#phone')
    ADD_STREET1_INPUT = (By.CSS_SELECTOR, '#street1')
    ADD_STREET2_INPUT = (By.CSS_SELECTOR, '#street2')
    ADD_CITY_INPUT = (By.CSS_SELECTOR, '#city')
    ADD_STATE_PROVINCE_INPUT = (By.CSS_SELECTOR, '#stateProvince')
    ADD_POSTAL_CODE_INPUT = (By.CSS_SELECTOR, '#postalCode')
    ADD_COUNTRY_INPUT = (By.CSS_SELECTOR, '#country')
