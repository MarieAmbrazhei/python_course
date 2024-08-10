from homework23.page.add_contact_page_locators import AddContactPageLocators
from homework23.page.page_urls import PageUrls
from homework25.base.base_page import BasePage


class AddContactPage(BasePage):
    """
    Represents the page for adding a new contact.
    """
    PAGE_URL = PageUrls.ADD_USER_PAGE_URL

    def __init__(self, driver):
        """
        Initialize the AddContactPage.
        """
        super().__init__(driver)

    def generate_contact_data(self):
        """
        Generate random contact data.
        """
        contact_list_data = {
            AddContactPageLocators.ADD_FIRSTNAME_INPUT: self.random.generate_random_first_name(),
            AddContactPageLocators.ADD_LASTNAME_INPUT: self.random.generate_random_last_name(),
            AddContactPageLocators.ADD_BIRTHDATE_INPUT: self.random.generate_random_dob(),
            AddContactPageLocators.ADD_EMAIL_INPUT: self.random.generate_random_email(),
            AddContactPageLocators.ADD_PHONE_INPUT: self.random.int_gen(length=6),
            AddContactPageLocators.ADD_STREET1_INPUT: self.random.generate_random_street_address(),
            AddContactPageLocators.ADD_STREET2_INPUT: self.random.generate_random_street_address(),
            AddContactPageLocators.ADD_CITY_INPUT: self.random.generate_random_city(),
            AddContactPageLocators.ADD_STATE_PROVINCE_INPUT: self.random.generate_random_state(),
            AddContactPageLocators.ADD_POSTAL_CODE_INPUT: self.random.generate_random_postcode(),
            AddContactPageLocators.ADD_COUNTRY_INPUT: self.random.generate_random_country()
        }
        return contact_list_data
