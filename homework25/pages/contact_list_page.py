from homework25.base.base_page import BasePage
from homework23.page.page_urls import PageUrls
from homework23.page.contact_list_page_locators import ContactListPageLocators


class ContactListPage(BasePage):
    """
    Represents the page displaying a list of contacts.
    """
    PAGE_URL = PageUrls.CONTACT_LIST_PAGE_URL

    def __init__(self, driver):
        """
        Initialize the ContactListPage.
        """
        super().__init__(driver)

    def click_add_new_contact(self):
        """
        Click the button to add a new contact.
        """
        self.click_button(ContactListPageLocators.ADD_NEW_CONTACT_BUTTON)
