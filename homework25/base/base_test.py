import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pymar_logger import logger as log
from homework25.pages.contact_list_page import ContactListPage
from homework25.pages.login_page import LoginPage
from homework25.pages.add_user_page import AddUserPage
from homework25.pages.contact_details_page import ContactDetailsPage
from homework25.pages.add_contact_page import AddContactPage
from homework25.pages.edit_contact_page import EditContactPage
from homework23.page.login_page_locators import LoginPageLocators
from homework23.page.common_page_locators import CommonPageLocators
from homework23.page.contact_list_page_locators import ContactListPageLocators
from homework23.page.add_contact_page_locators import AddContactPageLocators
from homework23.page.contact_edit_page_locators import EditContactPageLocators


class BaseTest:
    """
    Base class for test cases involving contact management.

    Provides setup and utility methods for tests that interact with the application's
    user and contact management features. This class initializes page objects and
    provides methods for adding and editing contacts.
    """
    login_page: LoginPage
    add_user_page: AddUserPage
    contact_list_page: ContactListPage
    add_contact_page: AddContactPage
    contact_details_page: ContactDetailsPage
    edit_contact_page: EditContactPage
    driver: WebDriver

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """
        Set up the test environment.
        """
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.add_user_page = AddUserPage(driver)
        self.contact_list_page = ContactListPage(driver)
        self.add_contact_page = AddContactPage(driver)
        self.contact_details_page = ContactDetailsPage(driver)
        self.edit_contact_page = EditContactPage(driver)

    def add_new_contact(self):
        """
        Test the ability to add a contact.
        """
        log.info("Opening login page")
        self.login_page.open()
        log.info("Verifying login page is opened")
        self.login_page.is_opened()
        log.info("Clicking on sign-up button")
        self.login_page.click_button(LoginPageLocators.LOGIN_SIGN_UP_BUTTON)
        log.info("Verifying add user page is opened")
        self.add_user_page.is_opened()
        log.info("Adding a new user")
        self.add_user_page.add_new_user()
        log.info("Submitting new user form")
        self.add_user_page.click_button(CommonPageLocators.LOCATOR_SUBMIT_BUTTON)
        log.info("Verifying contact list page is opened")
        self.contact_list_page.is_opened()
        log.info("Clicking on 'Add new contact' button")
        self.contact_list_page.click_add_new_contact()
        log.info("Creating a contact")
        email = (self.add_contact_page.insert_contact_data
                 (selector=AddContactPageLocators.ADD_EMAIL_INPUT))
        log.info("Submitting new contact form")
        self.add_contact_page.click_button(CommonPageLocators.LOCATOR_SUBMIT_BUTTON)
        log.info("Verifying contact list page is reopened")
        self.contact_list_page.is_opened()
        return email

    def edit_contact(self, email):
        """
        Test the ability to edit a contact.
        """
        log.info("Finding user with exact email: %s", email)
        found_email_el = self.add_contact_page.find_user_with_exact_email(
            email=email,
            selector=ContactListPageLocators.CONTACT_TABLE_EXACT_EMAIL)
        log.info("Clicking on found email element to open contact details")
        self.contact_list_page.click_web_element(found_email_el)
        log.info("Verifying contact details page is opened")
        self.contact_details_page.is_opened()
        log.info("Clicking on 'Edit contact' button")
        self.contact_details_page.click_edit_contact()
        log.info("Verifying edit contact page is opened")
        self.edit_contact_page.is_opened()
        log.info("Waiting for first name input field to be ready")
        self.edit_contact_page.wait_element(attr='#firstName')
        log.info("Updating a contact")
        updated_email = (self.edit_contact_page.insert_contact_data
                         (selector=EditContactPageLocators.ADD_EMAIL_INPUT))
        log.info("Submitting updated contact form")
        self.add_contact_page.click_button(CommonPageLocators.LOCATOR_SUBMIT_BUTTON)
        log.info("Verifying contact details page is reopened")
        self.contact_details_page.is_opened()
        log.info("Returning to contact list")
        self.contact_details_page.click_return_contact_list()
        log.info("Verifying contact list page is reopened")
        self.contact_list_page.is_opened()
        return updated_email
