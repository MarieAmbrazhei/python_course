"""Login page page"""
from selenium.webdriver.common.by import By


class LoginPage:
    """
    Class store login page locators
    """
    LOGIN_EMAIL_INPUT = By.CSS_SELECTOR, '#email'
    LOGIN_PASSWORD_INPUT = By.CSS_SELECTOR, '#password'
    LOGIN_SIGN_UP_BUTTON = By.CSS_SELECTOR, '#signup'
