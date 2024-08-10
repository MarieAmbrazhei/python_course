from homework23.page.add_contact_page_locators import AddContactPageLocators
from homework23.page.contact_edit_page_locators import ContactEdit

URL = 'https://thinking-tester-contact-list.herokuapp.com/'
EMAIL = 'test@uuu.com'
PASSWORD = '1234567'

contact_list_data = {
    AddContactPageLocators.ADD_FIRSTNAME_INPUT: 'Marie',
    AddContactPageLocators.ADD_LASTNAME_INPUT: 'Ambrazhei',
    AddContactPageLocators.ADD_BIRTHDATE_INPUT: '1992-01-01',
    AddContactPageLocators.ADD_EMAIL_INPUT: 'mary@hel.com',
    AddContactPageLocators.ADD_PHONE_INPUT: '12345678',
    AddContactPageLocators.ADD_STREET1_INPUT: '21 Lvivo',
    AddContactPageLocators.ADD_STREET2_INPUT: '2 Lvivo',
    AddContactPageLocators.ADD_CITY_INPUT: 'Vilnius',
    AddContactPageLocators.ADD_STATE_PROVINCE_INPUT: 'Vilnius',
    AddContactPageLocators.ADD_POSTAL_CODE_INPUT: '123456',
    AddContactPageLocators.ADD_COUNTRY_INPUT: 'Lithuania',
}

updated_contact_list_data = {
    ContactEdit.ADD_FIRSTNAME_INPUT: 'Darya',
    ContactEdit.ADD_LASTNAME_INPUT: 'Abramovich',
    ContactEdit.ADD_BIRTHDATE_INPUT: '1992-01-01',
    ContactEdit.ADD_EMAIL_INPUT: 'mary@hel.com',
    ContactEdit.ADD_PHONE_INPUT: '87654321',
    ContactEdit.ADD_STREET1_INPUT: '3 Lvivo',
    ContactEdit.ADD_STREET2_INPUT: '4 Lvivo',
    ContactEdit.ADD_CITY_INPUT: 'Minsk',
    ContactEdit.ADD_STATE_PROVINCE_INPUT: 'Belarus',
    ContactEdit.ADD_POSTAL_CODE_INPUT: '654393',
    ContactEdit.ADD_COUNTRY_INPUT: 'Belarus',
}
