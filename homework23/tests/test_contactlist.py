"""Homework23: Selenium locators"""

from homework23.pages.add_contact_page_locators import AddContactPage
from homework23.pages.login_page_locators import LoginPage
from homework23.pages.contact_list_page_locators import ContactListPage
from homework23.pages.add_user_page_locators import AddUserPage
from homework23.pages.common_page_locators import CommonPageLocators
from homework23.pages.contact_details_page import ContactDetails
from homework23.pages.contact_edit_page_locators import ContactEdit
from homework23.pages.page_urls import PageUrls

# Open your web browser
print(f'Open the login page: {PageUrls.LOGIN_PAGE_URL}')
# LOGIN PAGE
# Click "Signup" button
print(f'Click Signup button:  {LoginPage.LOGIN_SIGN_UP_BUTTON}')
# ADD NEW USER PAGE
print(f'Fill in the first name field: {AddUserPage.ADD_FIRSTNAME_INPUT}')
print(f'Fill in the last name field: {AddUserPage.ADD_LASTNAME_INPUT}')
print(f'Fill in the email field: {AddUserPage.LOGIN_EMAIL_INPUT}')
print(f'Fill in the password field: {AddUserPage.LOGIN_PASSWORD_INPUT}')

print(f'Click Submit button: {CommonPageLocators.LOGIN_SUBMIT_BUTTON}')

# CONTACT LIST PAGE
print(f'Click Add a New Contact button: {ContactListPage.ADD_NEW_CONTACT_BUTTON}')
# ADD CONTACT PAGE
print(f'Fill in the first name field: {AddContactPage.ADD_FIRSTNAME_INPUT}')
print(f'Fill in the last name field: {AddContactPage.ADD_LASTNAME_INPUT}')
print(f'Fill in the date of birth field: {AddContactPage.ADD_BIRTHDATE_INPUT}')
print(f'Fill in the email field: {AddContactPage.ADD_EMAIL_INPUT}')
print(f'Fill in the phone field: {AddContactPage.ADD_PHONE_INPUT}')
print(f'Fill in the street address 1 field: {AddContactPage.ADD_STREET1_INPUT}')
print(f'Fill in the street address 2 field: {AddContactPage.ADD_STREET2_INPUT}')
print(f'Fill in the city field: {AddContactPage.ADD_CITY_INPUT}')
print(f'Fill in the state of province field: {AddContactPage.ADD_STATE_PROVINCE_INPUT}')
print(f'Fill in the postal code field: {AddContactPage.ADD_POSTAL_CODE_INPUT}')
print(f'Fill in the country field: {AddContactPage.ADD_COUNTRY_INPUT}')

print(f'Click Submit button: {CommonPageLocators.LOGIN_SUBMIT_BUTTON}')

# Add another contact
# CONTACT LIST PAGE
print(f'Click Add a New Contact button: {ContactListPage.ADD_NEW_CONTACT_BUTTON}')
# ADD CONTACT PAGE
print(f'Fill in the first name field: {AddContactPage.ADD_FIRSTNAME_INPUT}')
print(f'Fill in the last name field: {AddContactPage.ADD_LASTNAME_INPUT}')
print(f'Fill in the date of birth field: {AddContactPage.ADD_BIRTHDATE_INPUT}')
print(f'Fill in the email field: {AddContactPage.ADD_EMAIL_INPUT}')
print(f'Fill in the phone field: {AddContactPage.ADD_PHONE_INPUT}')
print(f'Fill in the street address 1 field: {AddContactPage.ADD_STREET1_INPUT}')
print(f'Fill in the street address 2 field: {AddContactPage.ADD_STREET2_INPUT}')
print(f'Fill in the city field: {AddContactPage.ADD_CITY_INPUT}')
print(f'Fill in the state of province field: {AddContactPage.ADD_STATE_PROVINCE_INPUT}')
print(f'Fill in the postal code field: {AddContactPage.ADD_POSTAL_CODE_INPUT}')
print(f'Fill in the country field: {AddContactPage.ADD_COUNTRY_INPUT}')

print(f'Click Submit button: {CommonPageLocators.LOGIN_SUBMIT_BUTTON}')

# Edit contact
# CONTACT LIST PAGE
print(f'Click on the first contact row: {ContactListPage.CONTACT_TABLE_FIRST_ROW}')
# CONTACT SELECTED DETAILS PAGE
print(f'Click on Edit Contact button: {ContactDetails.EDIT_CONTACT_BUTTON}')
# EDIT CONTACT PAGE
print(f'Fill in the first name field: {ContactEdit.ADD_FIRSTNAME_INPUT}')
print(f'Fill in the last name field: {ContactEdit.ADD_LASTNAME_INPUT}')
print(f'Fill in the date of birth field: {ContactEdit.ADD_BIRTHDATE_INPUT}')
print(f'Fill in the email field: {ContactEdit.ADD_EMAIL_INPUT}')
print(f'Fill in the phone field: {ContactEdit.ADD_PHONE_INPUT}')
print(f'Fill in the street address 1 field: {ContactEdit.ADD_STREET1_INPUT}')
print(f'Fill in the street address 2 field: {ContactEdit.ADD_STREET2_INPUT}')
print(f'Fill in the city field: {ContactEdit.ADD_CITY_INPUT}')
print(f'Fill in the state of province field: {ContactEdit.ADD_STATE_PROVINCE_INPUT}')
print(f'Fill in the postal code field: {ContactEdit.ADD_POSTAL_CODE_INPUT}')
print(f'Fill in the country field: {ContactEdit.ADD_COUNTRY_INPUT}')

print(f'Click Submit button: {CommonPageLocators.LOGIN_SUBMIT_BUTTON}')

# CONTACT DETAILS PAGE
print(f'Click Return to Contact List: {ContactDetails.RETURN_TO_CONTACT_LIST_BUTTON}')

# Delete contact
# CONTACT LIST PAGE
print(f'Click on the second contact row: {ContactListPage.CONTACT_TABLE_SECOND_ROW}')
# CONTACT DETAILS PAGE
print(f'Click Delete Contact button: {ContactDetails.DELETE_CONTACT_BUTTON}')

# Logout
# CONTACT LIST PAGE
print(f'Click Logout button: {CommonPageLocators.LOGIN_LOGOUT_BUTTON}')

# Log in (if you have a user)
# LOGIN PAGE
print(f'Fill in the email field: {LoginPage.LOGIN_EMAIL_INPUT}')
print(f'Fill in the password field: {LoginPage.LOGIN_PASSWORD_INPUT}')

print(f'Click Submit button: {CommonPageLocators.LOGIN_SUBMIT_BUTTON}')
