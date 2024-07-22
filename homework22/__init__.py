# library_keywords.py

from homework12.homework12_1 import Book, User
from pymar_log import logger as log
from robot.api.deco import keyword


@keyword
def create_book(name, isbn, pages, author):
    """
    Create a Book instance with the provided details.
    """
    return Book(name, isbn, pages, author)


@keyword
def create_user(user_id):
    """
    Create a User instance with the provided user ID.
    """
    return User(user_id)


@keyword
def take_book(user, isbn):
    """
    User tries to take a book with the given ISBN.
    """
    return user.take_book(isbn)


@keyword
def reserve_book(user, isbn):
    """
    User tries to reserve a book with the given ISBN.
    """
    return user.reserve_book(isbn)


@keyword
def return_book(user, isbn):
    """
    User tries to return a book with the given ISBN.
    """
    return user.return_book(isbn)
