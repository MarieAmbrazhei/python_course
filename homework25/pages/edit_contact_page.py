from homework25.base.base_page import BasePage
from homework23.page.page_urls import PageUrls
from homework23.page.contact_edit_page_locators import EditContactPageLocators


class EditContactPage(BasePage):
    """
    Represents the page for editing contact information.
    """
    PAGE_URL = PageUrls.EDIT_CONTACT_URL

    def __init__(self, driver):
        """
        Initialize the EditContactPage.
        """
        super().__init__(driver)

    def generate_contact_data(self):
        """
        Generate random contact data.
        """

        contact_list_data = {
            EditContactPageLocators.ADD_FIRSTNAME_INPUT: self.random.generate_random_first_name(),
            EditContactPageLocators.ADD_LASTNAME_INPUT: self.random.generate_random_last_name(),
            EditContactPageLocators.ADD_BIRTHDATE_INPUT: self.random.generate_random_dob(),
            EditContactPageLocators.ADD_EMAIL_INPUT: self.random.generate_random_email(),
            EditContactPageLocators.ADD_PHONE_INPUT: self.random.int_gen(length=6),
            EditContactPageLocators.ADD_STREET1_INPUT: self.random.generate_random_street_address(),
            EditContactPageLocators.ADD_STREET2_INPUT: self.random.generate_random_street_address(),
            EditContactPageLocators.ADD_CITY_INPUT: self.random.generate_random_city(),
            EditContactPageLocators.ADD_STATE_PROVINCE_INPUT: self.random.generate_random_state(),
            EditContactPageLocators.ADD_POSTAL_CODE_INPUT: self.random.generate_random_postcode(),
            EditContactPageLocators.ADD_COUNTRY_INPUT: self.random.generate_random_country()
        }
        return contact_list_data
