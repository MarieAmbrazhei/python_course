from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

url = 'https://thinking-tester-contact-list.herokuapp.com/'


@pytest.fixture()
def browser_open():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(url)
    yield browser
    browser.quit()


def test_login():
    pass
