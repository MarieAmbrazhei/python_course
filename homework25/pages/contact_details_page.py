from homework25.base.base_page import BasePage
from homework23.page.page_urls import PageUrls
from homework23.page.contact_details_page_locators import ContactDetailsLocators


class ContactDetailsPage(BasePage):
    """
    Represents the page displaying details of a specific contact.
    """
    PAGE_URL = PageUrls.CONTACT_DETAILS_URL

    def __init__(self, driver):
        """
        Initialize the ContactDetailsPage.
        """
        super().__init__(driver)

    def click_edit_contact(self):
        """
        Click the button to edit the contact details.
        """
        self.click_button(ContactDetailsLocators.EDIT_CONTACT_BUTTON)

    def click_delete_contact_button(self):
        """
        Click the button to delete the contact.
        """
        self.click_button(ContactDetailsLocators.DELETE_CONTACT_BUTTON)

    def click_return_contact_list(self):
        """
        Click the button to return to the contact list page.
        """
        self.click_button(ContactDetailsLocators.RETURN_TO_CONTACT_LIST_BUTTON)
