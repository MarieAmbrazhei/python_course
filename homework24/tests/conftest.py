import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework23.page.login_page_locators import LoginPage
from homework23.page.common_page_locators import CommonPageLocators
from homework24.resources.constants import URL, EMAIL, PASSWORD


@pytest.fixture()
def browser_session():
    """
    Fixture function that opens a browser and navigates to a specified URL
    """

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    # options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get(URL)
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def login(wait):
    """
    Logs in to the web page.
    """

    email_field = wait.until(
        EC.presence_of_element_located(LoginPage.LOGIN_EMAIL_INPUT))
    email_field.send_keys(EMAIL)

    password_field = wait.until(
        EC.presence_of_element_located(LoginPage.LOGIN_PASSWORD_INPUT))
    password_field.send_keys(PASSWORD)

    btn_submit = wait.until(
        EC.element_to_be_clickable(CommonPageLocators.LOCATOR_SUBMIT_BUTTON))
    btn_submit.click()


@pytest.fixture
def wait(browser_session) -> WebDriverWait:
    """
    Fixture that provides an instance of WebDriverWait with a timeout of 10 seconds.
    """
    return WebDriverWait(browser_session, 10)
