from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from homework23.page.add_contact_page_locators import AddContactPage
from homework23.page.contact_edit_page_locators import ContactEdit
from homework23.page.common_page_locators import CommonPageLocators
from homework23.page.contact_details_page_locators import ContactDetails
from homework23.page.contact_list_page_locators import ContactListPage
from homework24.resources.constants import updated_contact_list_data
from homework24.resources.utils import fill_field, random_int, generate_contact_data
from pymar_logger import logger as log
import pytest


def test_delete_record(browser_session, wait):
    counter = 0
    while elem := wait.until(
            EC.element_to_be_clickable(ContactListPage.CONTACT_TABLE_FIRST_ROW)):
        elem.click()
        button = wait.until(EC.element_to_be_clickable(ContactDetails.DELETE_CONTACT_BUTTON))
        button.click()
        alert = browser_session.switch_to.alert
        alert.accept()
        counter += 1
        print(f'deleted records: {counter}')


@pytest.mark.parametrize('count', range(100))
def test_add_contacts(wait, count):
    """
    Adds a new contact to the contact list.
    """
    log.info("Starting verification that a user can add a contact with all required fields.")
    btn_add_contact = wait.until(
        EC.element_to_be_clickable(ContactListPage.ADD_NEW_CONTACT_BUTTON)
    )
    btn_add_contact.click()
    contact_list_data = generate_contact_data()
    list(map(lambda item: fill_field(wait, *item), contact_list_data.items()))

    btn_submit = wait.until(
        EC.element_to_be_clickable(CommonPageLocators.LOCATOR_SUBMIT_BUTTON)
    )
    btn_submit.click()
    # time.sleep(1000)

    contact_table_row = wait.until(
        EC.presence_of_element_located(ContactListPage.CONTACT_TABLE_FIRST_ROW)
    )
    log.info("New contact row located in the contact list.")
    contact_table_row.click()
    assert contact_table_row is not None
    log.info("Contact addition verified successfully.")


def test_edit_contact(browser_session, wait):
    """
    Edit a new contact to the contact list.
    """
    log.info("Starting the process to edit an existing contact.")
    contact_table_row = wait.until(
        EC.element_to_be_clickable(ContactListPage.CONTACT_TABLE_FIRST_ROW)
    )
    contact_table_row.click()

    btn_edit_contact = wait.until(
        EC.element_to_be_clickable(ContactDetails.EDIT_CONTACT_BUTTON)
    )
    btn_edit_contact.click()
    # Wait until form is populated (JavaScript condition is true)
    wait.until(
        lambda driver: driver.execute_script(
            "return document.querySelector('#firstName').value !== '';")
    )

    for locator, value in updated_contact_list_data.items():
        input_field = wait.until(EC.element_to_be_clickable(locator))
        input_field.click()
        input_field.clear()
        input_field.send_keys(value)

    btn_submit = wait.until(
        EC.element_to_be_clickable(CommonPageLocators.LOCATOR_SUBMIT_BUTTON)
    )
    btn_submit.click()
    log.info("Waiting for the contact details to be updated.")
    # Wait until form is populated (JavaScript condition is true)
    wait.until(
        lambda driver: driver.execute_script(
            "return document.querySelector('#firstName').innerHTML !== '';")
    )

    email = browser_session.find_element(By.CSS_SELECTOR, '#email').text
    assert email == updated_contact_list_data.get(ContactEdit.ADD_EMAIL_INPUT)
    log.info("Email address verification successful.")


@pytest.mark.parametrize('count', list(range(1)))
def test_delete_contact(browser_session, wait, count):
    """
    Deletes a contact on a web page.
    """
    # add contact
    log.info("Starting the process to delete a contact.")
    btn_add_contact = wait.until(
        EC.element_to_be_clickable(ContactListPage.ADD_NEW_CONTACT_BUTTON)
    )
    btn_add_contact.click()

    random_tel_number = random_int()
    contact_list_data[AddContactPage.ADD_PHONE_INPUT] = random_tel_number

    list(map(lambda item: fill_field(wait, *item), updated_contact_list_data.items()))

    btn_submit = wait.until(
        EC.element_to_be_clickable(CommonPageLocators.LOCATOR_SUBMIT_BUTTON)
    )
    btn_submit.click()

    # delete contact
    contact_table_row = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, ContactListPage.CONTACT_TABLE_EXACT_NUMBER.format(random_tel_number))
        ))
    contact_table_row.click()
    btn_delete_contact = wait.until(
        EC.element_to_be_clickable(ContactDetails.DELETE_CONTACT_BUTTON)
    )
    btn_delete_contact.click()

    alert = browser_session.switch_to.alert
    alert.accept()
    log.info(f"Verifying that the contact with phone number {random_tel_number} has been deleted.")
    deleted_contact = browser_session.find_elements(
        *(By.XPATH, ContactListPage.CONTACT_TABLE_EXACT_NUMBER.format(random_tel_number)))
    assert deleted_contact == [], f'The contact with {random_tel_number} was found!'
    log.info("Contact deletion verified successfully.")
