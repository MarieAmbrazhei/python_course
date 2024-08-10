from typing import Tuple
from homework25.base.base_page import BasePage
from homework23.page.add_user_page_locators import AddUserPageLocators
from homework23.page.page_urls import PageUrls


class AddUserPage(BasePage):
    """
    Represents the page for adding a new user.
    """
    PAGE_URL = PageUrls.ADD_USER_PAGE_URL

    def __init__(self, driver):
        """
        Initialize the AddUserPage.
        """
        super().__init__(driver)

    def add_new_user(self) -> Tuple[str, str]:
        """
        Add a new user with randomly generated details.
        """
        login_email = self.random.generate_random_email()
        password = self.random.generate_random_password(length=10)

        self.fill_field(selector=AddUserPageLocators.ADD_FIRSTNAME_INPUT,
                        data=self.random.generate_random_first_name())
        self.fill_field(selector=AddUserPageLocators.ADD_LASTNAME_INPUT,
                        data=self.random.generate_random_last_name())
        self.fill_field(selector=AddUserPageLocators.LOGIN_EMAIL_INPUT,
                        data=login_email)
        self.fill_field(selector=AddUserPageLocators.LOGIN_PASSWORD_INPUT,
                        data=password)
        return login_email, password
