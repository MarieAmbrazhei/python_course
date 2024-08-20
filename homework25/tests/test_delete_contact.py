from pymar_logger import logger as log
from homework25.base.base_test import BaseTest
from homework23.page.contact_list_page_locators import ContactListPageLocators


class TestDeleteContact(BaseTest):
    """
    Class for deleting a contact.
    """

    def test_delete_contact(self):
        """
        Test the ability to delete a contact.
        """
        log.info("Finding a contact with exact email")
        email = self.add_new_contact()
        found_email_el = self.add_contact_page.find_user_with_exact_email(
            email=email, selector=ContactListPageLocators.CONTACT_TABLE_EXACT_EMAIL)
        log.info(f"Clicking on the contact with email: {email}")
        self.contact_list_page.click_web_element(found_email_el)
        log.info("Verifying that the contact details page is opened.")
        self.contact_details_page.is_opened()
        log.info("Clicking the 'Delete Contact' button.")
        self.contact_details_page.click_delete_contact_button()
        log.info("Confirming deletion in the alert.")
        self.contact_details_page.confirmation_alert_confirm()
        log.info("Verifying that the contact list page is reopened.")
        self.contact_list_page.is_opened()
        log.info(f"Verifying that the contact with email: {email} is no longer present.")
        self.contact_list_page.check_exact_email_not_present(
            email=email,
            selector=ContactListPageLocators.CONTACT_TABLE_EXACT_EMAIL)
