from selenium.webdriver.common.by import By

""" Contact list page page"""


class ContactListPageLocators:
    """
    Class store add contact list page locators
    """
    ADD_NEW_CONTACT_BUTTON = (By.CSS_SELECTOR, '#add-contact')
    CONTACT_TABLE_FIRST_ROW = (By.CSS_SELECTOR, '#myTable > .contactTableBodyRow:nth-child(3)')
    CONTACT_TABLE_SECOND_ROW = (By.CSS_SELECTOR, '#myTable > .contactTableBodyRow:nth-child(4)')
    CONTACT_TABLE_EXACT_NUMBER = (By.XPATH, "//tr[@class='contactTableBodyRow']/td[text()='{}']")
    CONTACT_TABLE_EXACT_EMAIL = (By.XPATH, "//td[text()='{email}']")
