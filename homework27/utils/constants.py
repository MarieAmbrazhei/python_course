"""Module contains API constants."""
CREATE_USER_ERRORS = {
    'name': 'Invalid name: it must be a string with at least 3 characters',
    'email': 'Invalid email address',
    'age': 'Invalid age: it must be a number between 18 and 120',
    'phoneNumber': 'Invalid phone number: it must be in the format +<country code> '
                   'followed by 7 to 10 digits',
    'address': 'Invalid address: it must be a string with at least 10 characters',
    'invalid_id': 'Invalid User ID format',
    'user_not_found': 'User not found',
    'no_empty_fields': 'At least one field is required for update'
}

INCORRECT_USER_ID = "000000000000000000000000"
