from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, \
    ElementClickInterceptedException, JavascriptException
from selenium.webdriver.remote.webelement import WebElement
from homework25.utils.utils import Randoms


class BasePage:
    """
    Base class for all page objects in the application.
    Provides common methods for interacting with web pages, such as opening pages,
    finding elements, clicking buttons, and filling fields. This class also includes
    utility methods for handling web elements and alerts.
    """
    PAGE_URL = None

    def __init__(self, driver):
        """
        Initialize the BasePage with a WebDriver instance.
        """
        self.driver: WebDriver = driver
        self.random = Randoms()
        self.wait = WebDriverWait(driver, 5, poll_frequency=1)

    def open(self):
        """
        Open the page using PAGE_URL.
        """
        if self.PAGE_URL is None:
            raise NotImplementedError("PAGE_URL must be defined in the subclass")
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        """
        Wait until the page URL matches PAGE_URL.
        """
        if self.PAGE_URL is None:
            raise NotImplementedError("PAGE_URL must be defined in the subclass")
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    def find_element(self, selector):
        """
        Find an element by its selector.
        """
        try:
            return self.driver.find_element(*selector)
        except NoSuchElementException:
            return None

    def find_element_visible(self, selector):
        """
        Find a visible element by its selector.
        """
        try:
            return self.wait.until(EC.visibility_of_element_located(selector))
        except (TimeoutException, NoSuchElementException):
            return None

    def click_button(self, selector):
        """
        Click a button specified by its selector.
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(selector))
            element.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
            print(f"Error: The element {selector} could not be clicked. Exception: {str(e)}")
            return None

    def fill_field(self, selector, data):
        """
        Fill a text field with data.
        """
        field = self.wait.until(EC.element_to_be_clickable(selector))
        field.clear()
        field.send_keys(data)

    def insert_contact_data(self, selector) -> str:
        """
        Insert contact data into fields and return the email.
        """
        contact_list_data = self.generate_contact_data()
        email = contact_list_data.get(selector)
        list(map(lambda item: self.fill_field(*item), contact_list_data.items()))
        return email

    def wait_element(self, attr):
        """
        Wait until the element with a specific attribute has a non-empty value.
        """
        try:
            self.wait.until(
                lambda driver: driver.execute_script(
                    f"return document.querySelector('{attr}').value !== '';"
                )
            )
        except (TimeoutException, JavascriptException) as e:
            print(
                f"Error: The element with selector {attr} did not meet the expected condition. "
                f"Exception: {str(e)}")
            return None

    def confirmation_alert_confirm(self):
        """
        Accept a confirmation alert and return its text.
        """
        alert = self.wait.until(EC.alert_is_present(),
                                message="Alert not found within the given time")
        alert_text = alert.text
        alert.accept()
        return alert_text

    def generate_contact_data(self):
        """
        Generate random contact data.
        """
        raise NotImplementedError

    def custom_wait(self, wait_time: int = 1) -> WebDriverWait:
        """
        Create a custom WebDriverWait instance.
        """
        return WebDriverWait(self.driver, wait_time, poll_frequency=1)

    @staticmethod
    def click_web_element(element: WebElement) -> None:
        """
        Click a WebElement.
        """
        element.click()

    def find_user_with_exact_email(self, email, selector):
        """
        Find a user with the exact email address.
        """
        element = self.find_element_visible(tuple(
            [selector[0], selector[1].format(email=email)]))
        assert element is not None, 'some error message for invalid result'
        return element

    def check_exact_email_not_present(self, email, selector):
        """
        Check that an email is not present on the page.
        """
        try:
            # Wait for a short time to ensure the element does not appear
            self.custom_wait().until(
                EC.presence_of_element_located(
                    (selector[0], selector[1].format(email=email))
                )
            )
            raise AssertionError('The email was found on the page, but it should not be present.')
        except TimeoutException:
            return True
