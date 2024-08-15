from pymar_logger import logger as log
from homework25.base.base_test import BaseTest
from homework23.page.contact_list_page_locators import ContactListPageLocators


class TestEditContact(BaseTest):
    """
    Class for editing a contact.
    """
    def test_edit_contact(self):
        """
        Test the ability to edit a contact.
        """
        log.info("Finding a contact with exact email")
        email = self.add_new_contact()
        updated_email = self.edit_contact(email=email)
        self.edit_contact_page.find_user_with_exact_email(
            email=updated_email,
            selector=ContactListPageLocators.CONTACT_TABLE_EXACT_EMAIL)
