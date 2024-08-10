from selenium.webdriver.common.by import By

""" Contact details page page """


class ContactDetailsLocators:
    """
    Class store contact details page locators
    """

    EDIT_CONTACT_BUTTON = (By.CSS_SELECTOR, '#edit-contact')
    DELETE_CONTACT_BUTTON = (By.CSS_SELECTOR, '#delete')
    RETURN_TO_CONTACT_LIST_BUTTON = (By.CSS_SELECTOR, '#return')