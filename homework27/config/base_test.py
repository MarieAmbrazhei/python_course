import pytest
from homework27.apis.users.api_users import UsersAPI

BASE_URL = 'https://alexqa.netlify.app/.netlify/'


class BaseTest:
    """
    BaseTest class to initialize the UsersAPI instance before each test.
    """
    api_users: UsersAPI

    @pytest.fixture(autouse=True)
    def setup_method(self, request):
        """
        Fixture to set up the UsersAPI instance before each test method.
        """
        if hasattr(request, 'param'):
            if request.param == 'not_create_user':
                self.api_users = UsersAPI(create_new_user=False)
            else:
                self.api_users = UsersAPI()
        else:
            self.api_users = UsersAPI()
