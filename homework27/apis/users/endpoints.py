"""Module contains Endpoints."""
HOST = 'https://alexqa.netlify.app/.netlify'


class Endpoints:
    """
    The Endpoints class provides a centralized collection of API endpoint URLs
    for user-related operations. It generates URLs for creating, retrieving,
    updating, deleting users, and checking user statuses.
    """
    create_user = f"{HOST}/functions/createUser"
    get_user_by_id = lambda self, uid: f"{HOST}/functions/getUser/{uid}"
    update_user_by_id = lambda self, uid: f"{HOST}/functions/updateUser/{uid}"
    delete_user_by_id = lambda self, uid: f"{HOST}/functions/deleteUser/{uid}"
    check_user_status_by_id = lambda self, uid: f"{HOST}/functions/checkUserStatus/{uid}"
    get_users = f"{HOST}/functions/getUsers"
    get_nonexistent_user_by_id = lambda self, uid: f"{HOST}functions/getUser/{uid}"
