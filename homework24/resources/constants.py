from homework23.page.add_contact_page_locators import AddContactPage
from homework23.page.contact_edit_page_locators import ContactEdit

URL = 'https://thinking-tester-contact-list.herokuapp.com/'
EMAIL = 'test@uuu.com'
PASSWORD = '1234567'

contact_list_data = {
    AddContactPage.ADD_FIRSTNAME_INPUT: 'Mary',
    AddContactPage.ADD_LASTNAME_INPUT: 'Ambrazhei',
    AddContactPage.ADD_BIRTHDATE_INPUT: '1991-01-01',
    AddContactPage.ADD_EMAIL_INPUT: 'mary@hello.com',
    AddContactPage.ADD_PHONE_INPUT: '12345678',
    AddContactPage.ADD_STREET1_INPUT: '1 Lvivo',
    AddContactPage.ADD_STREET2_INPUT: '2 Lvivo',
    AddContactPage.ADD_CITY_INPUT: 'Vilnius',
    AddContactPage.ADD_STATE_PROVINCE_INPUT: 'Vilnius',
    AddContactPage.ADD_POSTAL_CODE_INPUT: '123456',
    AddContactPage.ADD_COUNTRY_INPUT: 'Lithuania',
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

