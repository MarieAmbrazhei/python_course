import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def fill_field(wait, locator, value):
    """
    Fills an input field with the specified value.
    """
    input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
    input_field.send_keys(value)


def random_int() -> int:
    """
    Generates a random integer formed by concatenating shuffled digits from 1 to 10.
    """
    m_list = list(range(1, 11))
    random.shuffle(m_list)
    return int(''.join(map(str, m_list)))
