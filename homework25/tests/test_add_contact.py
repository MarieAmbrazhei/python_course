from pymar_logger import logger as log
from homework25.base.base_test import BaseTest
from homework23.page.contact_list_page_locators import ContactListPageLocators


class TestAddContact(BaseTest):
    """
    Class for adding a new contact.
    """
    def test_add_contact(self):
        """
        Test the ability to add a contact.
        """
        log.info("Finding a contact with exact email")
        email = self.add_new_contact()
        self.add_contact_page.find_user_with_exact_email(
            email=email,
            selector=ContactListPageLocators.CONTACT_TABLE_EXACT_EMAIL)
