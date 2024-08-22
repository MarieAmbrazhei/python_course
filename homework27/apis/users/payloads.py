from homework27.utils.random_methods import Randoms


class Payloads:
    """
    The Payloads class provides static methods for
    generating user-related payloads with random data.
    """

    @staticmethod
    def create_user():
        """
        Generates a payload for creating a new user with random data.
        """
        return {
            "name": Randoms.full_name(),
            "email": Randoms.email(),
            "age": Randoms.random_int(18, 120),
            "phoneNumber": f"+{Randoms.int_gen(length=8)}",
            "address": Randoms.street_address(),
            "role": Randoms.random_role(),
            "referralCode": Randoms.rand_word(length=8).upper()
        }

    @staticmethod
    def update_user():
        """
        Generates a payload for updating an existing user with random data.
        """
        return {
            "id": "",
            "name": Randoms.full_name(),
            "email": Randoms.email(),
            "age": Randoms.random_int(18, 120),
            "phoneNumber": f"+{Randoms.int_gen(length=8)}",
            "address": Randoms.street_address(),
            "role": Randoms.random_role(),
            "referralCode": Randoms.rand_word(length=8).upper()
        }
