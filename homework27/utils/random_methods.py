import random
import string
from faker import Faker

fake = Faker()


class Randoms:
    """
    The Randoms class provides a collection of static methods for generating random data.
    These methods are useful for generating test data such as random words, numbers,
    email addresses, and other personal information.
    """

    @staticmethod
    def rand_word(length: int) -> str:
        """
        Generates a random lowercase word of the specified length.
        """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def int_gen(length: int) -> str:
        """
        Generates a random string of digits with the specified length.
        """
        integers = string.digits
        return ''.join(random.choice(integers) for _ in range(length))

    @staticmethod
    def email_gen(length: int) -> str:
        """
        Generates a random email address with the local part being a random word of
        the specified length.
        """
        return f"{Randoms.rand_word(length)}@mail.com"

    @staticmethod
    def date_of_birth() -> str:
        """
        Generates a random date of birth in the format YYYY-MM-DD.
        """
        year = random.randint(1900, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year:04d}-{month:02d}-{day:02d}"

    @staticmethod
    def first_name() -> str:
        """
        Generates a random first name.
        """
        return fake.first_name()

    @staticmethod
    def last_name() -> str:
        """
        Generates a random last name.
        """
        return fake.last_name()

    @staticmethod
    def full_name():
        """
        Generates a random full name (first and last name).
        """
        return fake.name()

    @staticmethod
    def dob() -> str:
        """
        Generates a random date of birth in the format YYYY-MM-DD using
        Faker's date_of_birth method.
        """
        return fake.date_of_birth().strftime('%Y-%m-%d')

    @staticmethod
    def email() -> str:
        """
        Generates a unique random email address using Faker..
        """
        return fake.unique.email()

    @staticmethod
    def phone_number() -> str:
        """
        Generates a random phone number using Faker, truncated to a maximum of 15 characters.
        """
        return fake.phone_number()[:15]

    @staticmethod
    def street_address() -> str:
        """
        Generates a random street address using Faker.
        """
        return fake.street_address()

    @staticmethod
    def city() -> str:
        """
        Generates a random city name using Faker.
        """
        return fake.city()

    @staticmethod
    def state() -> str:
        """
        Generates a random state name using Faker.
        """
        return fake.state()

    @staticmethod
    def postcode() -> str:
        """
        Generates a random postal code using Faker.
        """
        return fake.postcode()

    @staticmethod
    def country() -> str:
        """
        Generates a random country name using Faker.
        """
        return fake.country()

    @staticmethod
    def random_int(min_age, max_age) -> int:
        """
        Generates a random integer between the specified minimum and maximum values.
        """
        return fake.random_int(min=min_age, max=max_age)

    @staticmethod
    def random_role():
        """
        Randomly selects a user role from a predefined list.
        """
        return random.choice(['user', 'admin', 'moderator'])

    @staticmethod
    def generate_random_alphanum_string(length: int) -> str:
        """
        Generates a random alphanumeric string of the specified length.
        """
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
