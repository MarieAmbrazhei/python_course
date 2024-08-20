import random
import string
from faker import Faker

fake = Faker()


class Randoms:
    """
    A utility class for generating random data.
    """

    @staticmethod
    def rand_word(length: int) -> str:
        """ Generate a random lowercase string."""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def int_gen(length: int) -> str:
        """ Generate a random digit string."""
        integers = string.digits
        return ''.join(random.choice(integers) for _ in range(length))

    @staticmethod
    def email_gen(length: int) -> str:
        """ Generate a random email address."""
        return f"{Randoms.rand_word(length)}@mail.com"

    @staticmethod
    def date_of_birth() -> str:
        """ Generate a random date of birth."""
        year = random.randint(1900, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)

        return f"{year:04d}-{month:02d}-{day:02d}"

    @staticmethod
    def generate_random_first_name() -> str:
        """ Generate a random first name."""
        return fake.unique.first_name()

    @staticmethod
    def generate_random_last_name() -> str:
        """ Generate a random last name."""
        return fake.unique.last_name()

    @staticmethod
    def generate_random_dob() -> str:
        """ Generate a random date of birth."""
        return fake.date_of_birth().strftime('%Y-%m-%d')

    @staticmethod
    def generate_random_email() -> str:
        """ Generate a random email address."""
        return fake.unique.email()

    @staticmethod
    def generate_random_phone_number() -> str:
        """ Generate a random phone number."""
        return fake.unique.phone_number()

    @staticmethod
    def generate_random_street_address() -> str:
        """ Generate a random street address."""
        return fake.unique.street_address()

    @staticmethod
    def generate_random_city() -> str:
        """ Generate a random city name."""
        return fake.unique.city()

    @staticmethod
    def generate_random_state() -> str:
        """ Generate a random state name. """
        return fake.unique.state()

    @staticmethod
    def generate_random_province() -> str:
        """ Generate a random province name."""
        return fake.unique.province()

    @staticmethod
    def generate_random_postcode() -> str:
        """ Generate a random postcode. """
        return fake.unique.postcode()

    @staticmethod
    def generate_random_country(length: int = 30) -> str:
        """ Generate a random country name."""
        return fake.unique.country()[:length]

    @staticmethod
    def generate_random_password(length: int) -> str:
        """ Generate a random password."""
        return ''.join(
            [random.choice(string.punctuation + string.ascii_letters) for _ in range(length)])
