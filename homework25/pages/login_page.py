from homework25.base.base_page import BasePage
from homework23.page.login_page_locators import LoginPageLocators
from homework23.page.common_page_locators import CommonPageLocators
from homework23.page.page_urls import PageUrls


class LoginPage(BasePage):
    """
    Represents the login page of the application.

    Provides methods to interact with the login page, including entering email,
    password, and submitting the login form.
    """
    PAGE_URL = PageUrls.LOGIN_PAGE_URL

    def __init__(self, driver):
        """
        Initialize the LoginPage.
        """
        super().__init__(driver)

    def enter_emai(self, email):
        """
        Enter email into the email field.
        """
        email_field = self.find_element(LoginPageLocators.LOGIN_EMAIL_INPUT)
        email_field.send_keys(email)

    def enter_password(self, pswrd):
        """
        Enter password into the password field.
        """
        pwd_field = self.find_element(LoginPageLocators.LOGIN_PASSWORD_INPUT)
        pwd_field.send_keys(pswrd)

    def complete_login(self, email, pswrd):
        """
        Perform the login action with email and password.
        """
        self.enter_emai(email)
        self.enter_password(pswrd)
        self.click_button(CommonPageLocators.LOCATOR_SUBMIT_BUTTON)
