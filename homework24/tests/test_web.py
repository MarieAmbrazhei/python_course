from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from homework23.page.login_page_locators import LoginPage
from homework23.page.common_page_locators import CommonPageLocators
from homework23.page.contact_details_page import ContactDetails
from homework23.page.add_contact_page_locators import AddContactPage
from homework23.page.contact_list_page_locators import ContactListPage
from homework23.page.contact_edit_page_locators import ContactEdit
import time

URL = 'https://thinking-tester-contact-list.herokuapp.com/'
EMAIL = 'test@uuu.com'
PASSWORD = '1234567'


@pytest.fixture()
def browser_session():
    """
    Fixture function that opens a browser and navigates to a specified URL
    """
    browser = webdriver.Chrome()
    browser.get(URL)
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def login(browser_session):
    """
    Logs in to the web page.
    """
    browser = browser_session
    explicit_wait = WebDriverWait(browser, 10)

    email_field = explicit_wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, LoginPage.LOGIN_EMAIL_INPUT)))
    email_field.send_keys(EMAIL)

    password_field = explicit_wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, LoginPage.LOGIN_PASSWORD_INPUT)))
    password_field.send_keys(PASSWORD)

    btn_submit = explicit_wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, CommonPageLocators.LOCATOR_SUBMIT_BUTTON)))
    btn_submit.click()


def fill_field(explicit_wait, locator, value):
    input_field = explicit_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
    input_field.send_keys(value)


def test_add_contact(browser_session):
    """
    Adds a new contact to the contact list.
    """
    browser = browser_session
    explicit_wait = WebDriverWait(browser, 10)

    btn_add_contact = explicit_wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ContactListPage.ADD_NEW_CONTACT_BUTTON))
    )
    btn_add_contact.click()

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

    list(map(lambda item: fill_field(explicit_wait, *item), contact_list_data.items()))

    btn_submit = explicit_wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, CommonPageLocators.LOCATOR_SUBMIT_BUTTON))
    )
    btn_submit.click()

    contact_table_row = explicit_wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ContactListPage.CONTACT_TABLE_FIRST_ROW))
    )
    contact_table_row.click()
    assert contact_table_row is not None


def test_edit_contact(browser_session):
    """
    Edit a new contact to the contact list.
    """
    browser = browser_session
    explicit_wait = WebDriverWait(browser, 10)

    contact_table_row = explicit_wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ContactListPage.CONTACT_TABLE_FIRST_ROW))
    )
    contact_table_row.click()

    btn_edit_contact = explicit_wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ContactDetails.EDIT_CONTACT_BUTTON))
    )
    btn_edit_contact.click()

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
    for locator, value in updated_contact_list_data.items():
        input_field = explicit_wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, locator)
        ))
        input_field.clear()
        input_field.send_keys(value)

    btn_submit = explicit_wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, CommonPageLocators.LOCATOR_SUBMIT_BUTTON))
    )
    btn_submit.click()
    time.sleep(1)

    email = browser.find_element(
        By.CSS_SELECTOR, '[id="email"]').text
    assert email == 'mary@hel.com'


def test_delete_contact(browser_session):
    """
    Deletes a contact on a web page.
    """
    browser = browser_session
    explicit_wait = WebDriverWait(browser, 10)

    contact_table_row = explicit_wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ContactListPage.CONTACT_TABLE_FIRST_ROW))
    )
    contact_table_row.click()

    btn_delete_contact = explicit_wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ContactDetails.DELETE_CONTACT_BUTTON))
    )
    btn_delete_contact.click()

    alert = browser_session.switch_to.alert
    alert.accept()

    try:
        btn_confirm_delete = explicit_wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ContactDetails.DELETE_CONTACT_BUTTON))
        )
        btn_confirm_delete.click()
    except TimeoutException:
        pass

