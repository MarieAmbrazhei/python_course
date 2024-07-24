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


@keyword
def release_book(user, isbn):
    """
    User tries to release a reserved book with the given ISBN.
    """
    return user.release_book(isbn)


@keyword
def log_message(message):
    """
    Log a message using the custom logger.
    """
    log.info(message)


@keyword
def check_if_book_in_taken_books(book, isbn):
    """
    Check if a book with the given ISBN is in the taken books list.
    """
    return isbn in book.taken_books


@keyword
def check_if_book_in_reserved_books(book, isbn):
    """
    Check if a book with the given ISBN is in the reserved books list.
    """
    return isbn in book.reserved_books


@keyword
def check_user_books(user, isbn):
    """
    Check if a book with the given ISBN is in the user's books.
    """
    return isbn in user.users_books.get(user.user_id, [])
