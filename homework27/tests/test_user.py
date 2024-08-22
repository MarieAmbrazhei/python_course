import pytest
from homework27.config.base_test import BaseTest
from homework27.utils import constants
from homework27.utils.constants import CREATE_USER_ERRORS
from homework27.utils.random_methods import Randoms
from pymar_logger import logger as log


class TestUsers(BaseTest):
    """
    Test suite for user-related API operations.
    """

    @pytest.mark.users
    def test_create_user(self):
        """
        Test the creation of a user.
        Asserts that the user creation response status is 'created'.
        """
        log.info("Starting test_create_user")
        response = self.api_users.user
        log.debug(f"Create user response: {response}")
        assert response.status == 'created', (
            f'Expected status is "created" but got {response.status}'
        )
        log.info("Finished test_create_user")

    @pytest.mark.users
    def test_get_user(self):
        """
        Test retrieval of a user by ID.
        Asserts that the retrieved user ID matches the expected user ID.
        """
        log.info("Starting test_get_user")
        user = self.api_users.user
        response = self.api_users.get_user_by_id(user.id)
        log.debug(f"Expected user ID: {user.id}, Retrieved user ID: {response.id}")
        assert user.id == response.id, (
            f'Expected User ID is {user.id} but got {response.id}'
        )
        log.info("Finished test_get_user")

    @pytest.mark.users
    def test_update_user(self):
        """
        Test updating a user by ID.
        Asserts that the update response status is 'updated'.
        """
        log.info("Starting test_update_user")
        user = self.api_users.user
        response = self.api_users.update_user_by_id(user_id=user.id)
        log.debug(f"Update user response: {response}")
        assert response.status == 'updated', (
            f'Expected status is "updated" but got {response.status}'
        )
        log.info("Finished test_update_user")

    # 404 error!!! Please check test_delete_created_user
    @pytest.mark.users
    @pytest.mark.xfail
    def test_delete_user(self):
        """
        Test deleting a user by ID.
        Expects the status code to be 200, but the test is expected to fail.
        """
        log.info("Starting test_delete_user")
        user = self.api_users.user
        response = self.api_users.delete_user_by_id(user_id=user.id)
        log.debug(f"Delete user response status code: {response.status_code}")
        assert response.status_code == 200, (
            f"Expected status code 200, but got {response.status_code}"
        )
        log.info("Finished test_delete_user")

    @pytest.mark.users
    def test_check_user_status(self):
        """
        Test checking the status of a user by ID.
        Asserts that the user status is 'created'.
        """
        log.info("Starting test_check_user_status")
        user = self.api_users.user
        response = self.api_users.check_user_status_by_id(user_id=user.id)
        log.debug(f"User status response: {response.status}")
        assert response.status == 'created', (
            f'Expected status is "created" but got {response.status}'
        )
        log.info("Finished test_check_user_status")

    @pytest.mark.users
    def test_get_users(self):
        """
        Test retrieval of the list of users.
        Asserts that the list of users is not empty.
        """
        log.info("Starting test_get_users")
        response = self.api_users.get_users()
        log.debug(f"Users list response: {response.users}")
        assert response.users, (
            f'List of users should contain users, but got {response.users}'
        )
        log.info("Finished test_get_users")

    @pytest.mark.users
    @pytest.mark.parametrize('setup_method', ['not_create_user'], indirect=True)
    @pytest.mark.parametrize('user_attr_to_delete', ['name', 'email', 'age', 'phoneNumber',
                                                     'address'])
    def test_create_user_incorrect_data(self, setup_method, user_attr_to_delete):
        """
        Test creating a user with invalid data by deleting specific attributes.
        Asserts that the error message matches the expected error for the given attribute.
        """
        log.info("Starting test_create_user_incorrect_data")
        log.debug(f"Setup method: {setup_method}, Attribute to delete: {user_attr_to_delete}")
        response = self.api_users.create_user_with_invalid_data(user_attr_to_delete)
        log.debug(f"Create user with invalid data response: {response.error_message}")
        assert response.error_message == CREATE_USER_ERRORS.get(user_attr_to_delete), (
            f'Expected error message for {user_attr_to_delete} but got {response.error_message}'
        )
        log.info("Finished test_create_user_incorrect_data")

    @pytest.mark.users
    @pytest.mark.parametrize('setup_method', ['not_create_user'], indirect=True)
    def test_get_user_with_nonexistent_id(self, setup_method):
        """
        Test retrieving a user with a nonexistent ID.
        Asserts that the error message matches the expected error for a nonexistent user.
        """
        log.info("Starting test_get_user_with_nonexistent_id")
        response = self.api_users.get_user_with_nonexistent_id(
            incorrect_user_id=constants.INCORRECT_USER_ID)
        log.debug(f"Get user with nonexistent ID response: {response.error_message}")
        assert response.error_message == CREATE_USER_ERRORS.get('user_not_found'), (
            f'Expected error message for nonexistent user but got {response.error_message}'
        )
        log.info("Finished test_get_user_with_nonexistent_id")

    @pytest.mark.users
    @pytest.mark.parametrize('setup_method', ['not_create_user'], indirect=True)
    def test_get_user_with_invalid_id(self, setup_method):
        """
        Test retrieving a user with an invalid ID.
        Asserts that the error message matches the expected error for an invalid ID.
        """
        log.info("Starting test_get_user_with_invalid_id")
        invalid_id = Randoms().generate_random_alphanum_string(length=20)
        response = self.api_users.get_user_with_invalid_id(invalid_id=invalid_id)
        log.debug(f"Get user with invalid ID response: {response.error_message}")
        assert response.error_message == CREATE_USER_ERRORS.get('invalid_id'), (
            f'Expected error message for invalid ID but got {response.error_message}'
        )
        log.info("Finished test_get_user_with_invalid_id")

    @pytest.mark.users
    def test_update_no_users_fields(self):
        """
        Test updating a user with no fields set.
        Asserts that the error message matches the expected error for missing fields.
        """
        log.info("Starting test_update_no_users_fields")
        user = self.api_users.user
        response = self.api_users.update_no_users_fields(user_id=user.id)
        log.debug(f"Update no users fields response: {response.error_message}")
        assert response.error_message == CREATE_USER_ERRORS.get('no_empty_fields'), (
            f'Expected error message for no empty fields but got {response.error_message}'
        )
        log.info("Finished test_update_no_users_fields")
