import requests
from homework27.apis.users.endpoints import Endpoints
from homework27.apis.users.payloads import Payloads
from homework27.config.headers import Headers
from homework27.apis.users.response_model import (
    UserResponseModel,
    UserGetResponseModel,
    UserDeleteResponseModel,
    UserStatusCheckResponseModel,
    UsersGetResponseModel,
    UserUpdateResponseModel,
)
from homework27.apis.users.request_model import UserRequestModel, UserUpdateRequestModel
from homework27.utils.response_error import ResponseError
from pymar_logger import logger as log


class UsersAPI:
    """
    UsersAPI class provides a set of methods for interacting with the user management API.
    This includes creating, updating, retrieving, and deleting users, as well as checking
    user statuses.
    """

    def __init__(self, create_new_user: bool = True):
        """
        Initialize the UsersAPI instance.
        """
        self.create_new_user = create_new_user
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()
        if self.create_new_user:
            self.user = self.create_user()

    def create_user(self):
        """
        Create a new user in the system.
        """
        log.info("Creating a new user.")
        request_data = UserRequestModel(**self.payloads.create_user())
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=request_data.model_dump()
        )
        log.debug(f"Create user response: {response.json()}")
        assert response.status_code == 200, response.json()
        model = UserResponseModel(**response.json())
        return model

    def get_user_by_id(self, user_id):
        """
        Retrieve user details by user ID.
        """
        log.info(f"Retrieving user with ID: {user_id}")
        response = requests.get(
            url=self.endpoints.get_user_by_id(user_id),
            headers=self.headers.basic,
        )
        log.debug(f"Get user by ID response: {response.json()}")
        assert response.status_code == 200, response.json()
        model = UserGetResponseModel(**response.json())
        return model

    def update_user_by_id(self, user_id):
        """
        Update user details by user ID.
        """
        log.info(f"Updating user with ID: {user_id}")
        update_payload = {**self.payloads.update_user(), "id": user_id}
        request_data = UserUpdateRequestModel(**update_payload)
        response = requests.put(
            url=self.endpoints.update_user_by_id(user_id),
            headers=self.headers.basic,
            json=request_data.model_dump()
        )
        log.debug(f"Update user by ID response: {response.json()}")
        assert response.status_code == 200, response.json()
        model = UserUpdateResponseModel(**response.json())
        return model

    def delete_user_by_id(self, user_id):
        """
        Delete a user by user ID.
        """
        log.info(f"Deleting user with ID: {user_id}")
        response = requests.delete(
            url=self.endpoints.delete_user_by_id(user_id),
            headers=self.headers.basic,
        )
        log.debug(f"Delete user by ID response: {response.json()}")
        assert response.status_code == 200, response.json()
        model = UserDeleteResponseModel(**response.json())
        return model

    def check_user_status_by_id(self, user_id):
        """
        Check the status of a user by user ID.
        """
        log.info(f"Checking status for user with ID: {user_id}")
        response = requests.get(
            url=self.endpoints.check_user_status_by_id(user_id),
            headers=self.headers.basic,
        )
        log.debug(f"Check user status by ID response: {response.json()}")
        assert response.status_code == 200, response.json()
        model = UserStatusCheckResponseModel(**response.json())
        return model

    def get_users(self):
        """
        Retrieve a list of all users.
        """
        log.info("Retrieving list of all users.")
        response = requests.get(
            url=self.endpoints.get_users,
            headers=self.headers.basic,
        )
        log.debug(f"Get users response: {response.json()}")
        assert response.status_code == 200, response.json()
        model = UsersGetResponseModel(**response.json())
        return model

    def create_user_with_invalid_data(self, exclude_field: str):
        """
        Attempt to create a user with invalid data by excluding a required field.
        """
        log.info(f"Creating user with invalid data, excluding field: {exclude_field}")
        request_data = UserRequestModel(**self.payloads.create_user())
        log.debug(f"Request data before exclusion: {request_data.model_dump()}")
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=request_data.model_dump(exclude={exclude_field})
        )
        log.debug(f"Create user with invalid data response: {response.json()}")
        assert response.status_code == 400, response.json()
        return ResponseError(response)

    def get_user_with_nonexistent_id(self, incorrect_user_id):
        """
        Attempt to retrieve a user with a non-existent ID.
        """
        log.info(f"Retrieving user with non-existent ID: {incorrect_user_id}")
        response = requests.get(
            url=self.endpoints.get_user_by_id(incorrect_user_id),
            headers=self.headers.basic,
        )
        log.debug(f"Get user with non-existent ID response: {response.json()}")
        assert response.status_code == 404, (f'Expected status code is "404", '
                                             f'but got {response.status_code}')
        return ResponseError(response)

    def get_user_with_invalid_id(self, invalid_id):
        """
        Attempt to retrieve a user with an invalid ID.
        """
        log.info(f"Retrieving user with invalid ID: {invalid_id}")
        response = requests.get(
            url=self.endpoints.get_user_by_id(invalid_id),
            headers=self.headers.basic,
        )
        log.debug(f"Get user with invalid ID response: {response.json()}")
        assert response.status_code == 400, (f'Expected status code is "400", '
                                             f'but got {response.status_code}')
        return ResponseError(response)

    def update_no_users_fields(self, user_id):
        """
        Attempt to update a user without providing any fields.
        """
        log.info(f"Attempting to update user with ID: {user_id} without any fields.")
        invalid_user_data = {}
        response = requests.put(
            url=self.endpoints.update_user_by_id(user_id),
            headers=self.headers.basic,
            json={**invalid_user_data, "id": user_id}
        )
        log.debug(f"Update no user fields response: {response.json()}")
        assert response.status_code == 400, (f'Expected status is '
                                             f'"400", but got {response.status_code}')
        return ResponseError(response)
