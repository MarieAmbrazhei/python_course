"""Add user page page"""
from selenium.webdriver.common.by import By


class AddUserPageLocators:
    """
    Class store add user page locators
    """

    ADD_FIRSTNAME_INPUT = (By.CSS_SELECTOR, '#firstName')
    ADD_LASTNAME_INPUT = (By.CSS_SELECTOR, '#lastName')
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, '#email')
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, '#password')
