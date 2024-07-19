"""Homework21_1: test_library_functionality"""

import pytest
from homework12.homework12_1 import Book, User
from pymar_logging import logger as log


@pytest.fixture
def setup_books():
    """Creates and deletes books"""
    Book.taken_books = []
    Book.reserved_books = []
    Book.books = {}

    book1 = Book("Learning Python", "134527", 1200,
                 "Mark Lutz")
    book2 = Book("Learn Python 3 the Hard Way", "234569",
                 1000, "Zed A. Shaw")
    book3 = Book("Think Python", "239874",
                 900, "Allen Downey ")

    yield book1, book2, book3
    del book1
    del book2
    del book3


@pytest.fixture
def user_1() -> User:
    """
    Creates and deletes user_1
    """
    user = User('user_id_1')
    yield user
    del user


@pytest.fixture
def user_2() -> User:
    """
    Creates and deletes user_2
    """
    user = User('user_id_2')
    yield user
    del user


def test_take_book_positive(user_1):
    """Test taking a book that is available."""
    log.info('User tries to take book with 134527 isbn')
    assert user_1.take_book('134527'), ('Failed to take the book with'
                                        ' ISBN 134527')
    assert '134527' in User.users_books[user_1.user_id], (
        'Book with ISBN 134527 is not in the user\'s taken books'
    )
    log.info('Successfully verified user can take book with ISBN 134527')


def test_take_book_already_taken(user_1, user_2):
    """Test that a user cannot take a book that is already taken."""
    log.info('User tries to take an already taken book with 134527 isbn')
    user_1.take_book('134527')
    log.info('User 2 tries to take already taken book with 134527 isbn')
    assert user_2.take_book('134527') is False, (
        'Failed to prevent User 2 from taking the book with ISBN 134527 '
        'that is already taken by User 1'
    )
    log.info(
        'Successfully verified user cannot take already taken book with ISBN '
        '134527')


def test_reserve_book_positive(user_1):
    """Test that a user can successfully reserve a book."""
    log.info('User tries to reserve book with c 234569 isbn')
    assert user_1.reserve_book('234569'), ('Failed to reserve the book with'
                                           ' ISBN 234569')
    assert '234569' in User.reserved_books, (
        'Book with ISBN 234569 is not in the reserved books list'
    )
    log.info(
        'Successfully verified user can reserve book with ISBN 234569'
        ' isbn')


def test_reserve_book_already_reserved(user_1, user_2):
    """Test that a user cannot reserve a book."""
    log.info('User tries to take an already reserved book with 234569 isbn')
    user_1.reserve_book('234569')
    log.info('User 2 tries to reserve already reserved book with 234569 isbn')
    assert user_2.reserve_book('234569') is False, (
        'Failed to prevent reserving a book with ISBN 234569 that is'
        ' already reserved')
    log.info(
        'Successfully verified user cannot reserve already reserved book '
        'with ISBN 134527 ')


def test_return_book_positive(user_1):
    """Test that a user can successfully return a book."""
    log.info('User tries to return book with 134527 isbn')
    user_1.take_book('134527')
    assert user_1.return_book('134527'), (
        'Failed to return the book with ISBN 134527'
    )
    assert '134527' not in User.taken_books, (
        'Book with ISBN 134527 should not be in the list of taken books'
        ' after return')

    log.info('Successfully verified user can return book with ISBN 134527')


def test_return_book_not_taken(user_2):
    """Test that a user cannot return a book that was not taken."""
    log.info('User tries to return a not taken book with 134527 isbn')
    assert user_2.return_book('134527') is False, (
        'User was able to return a book with ISBN 134527 that was not taken'
    )
    log.info(
        'Successfully verified user cannot return a book that was not'
        ' taken with ISBN 134527')


def test_release_book_positive(user_1):
    """Test that a user can successfully release a reserved book."""
    log.info('User tries to release book with 239874 isbn')
    user_1.reserve_book('239874')
    assert user_1.release_book('239874'), (
        'Failed to release the book with ISBN 239874'
    )
    assert '239874' not in User.reserved_books, (
        'Book with ISBN 239874 should not be in the list of '
        'taken books after return')

    log.info(
        'Successfully verified user can release reserved book with ISBN '
        ' 239874')


def test_release_book_not_reserved(user_2):
    """Test that a user cannot release a book that was not reserved."""
    log.info('User tries to release a not reserved book with 239874 isbn')
    assert user_2.release_book('239874') is False, (
        'User was able to release a book with ISBN 239874 that was not '
        'reserved'
    )
    log.info(
        'Successfully verified user cannot release a book that was not'
        ' reserved with ISBN  239874')


def test_take_invalid_book(user_1):
    """Test that a user cannot take a book that does not exist."""
    log.info('User tries to take a non-existent book with 111111 isbn')
    assert user_1.take_book('111111') is False, (
        'User was able to take a book with ISBN 111111 that does not exist'
    )
    log.info(
        'Successfully verified user cannot take a non-existent book with'
        ' ISBN 111111')


def test_reserve_invalid_book(user_1):
    """Test that a user cannot reserve a book that does not exist."""
    log.info('User tries to reserve a non-existent book with 111111 isbn')
    assert user_1.reserve_book('111111') is False, (
        'User was able to reserve a book with ISBN 111111 that does not exist'
    )
    log.info(
        'Successfully verified user cannot reserve a non-existent book with'
        ' ISBN  111111')


def test_return_invalid_book(user_1, ):
    """Test that a user cannot return a book that does not exist."""
    log.info('User tries to return a non-existent book with 111111 isbn')
    assert user_1.return_book('111111') is False, (
        'User was able to return a book with ISBN 111111 that does not exist'
    )
    log.info(
        'Successfully verified user can not return a non-existent book with '
        'ISBN 111111')


def test_release_invalid_book(user_1):
    """Test that a user cannot release a book that does not exist."""

    log.info('User tries to release a non-existent book with 111111 isbn')
    assert user_1.release_book('111111') is False, (
        'User was able to release a book with ISBN 111111 that does not exist'
    )
    log.info(
        'Successfully verified user cannot release a non-existent book with'
        'ISBN  111111')
