from selenium.webdriver.common.by import By

"""Common page page"""


class CommonPageLocators:
    """
    Class store common  page locators
    """

    LOCATOR_SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')
    LOCATOR_CANCEL_BUTTON = (By.CSS_SELECTOR, '#cancel')
    LOCATOR_LOGOUT_BUTTON = (By.CSS_SELECTOR, '#logout')
