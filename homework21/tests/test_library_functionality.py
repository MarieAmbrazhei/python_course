"""Homework21_2: test_library_functionality"""

from pymar_logging import logger as log
from constants import INCORRECT_ISBN


def test_take_book_positive(user_1, setup_books):
    """Test taking a book that is available."""
    book1, *_ = setup_books
    log.info(f'User tries to take book with {book1.isbn} isbn')
    assert user_1.take_book(book1.isbn), ('Failed to take the book with'
                                          f' ISBN {book1.isbn}')
    assert book1.isbn in user_1.users_books[user_1.user_id], (
        f'Book with ISBN {book1.isbn} is not in the user\'s taken books'
    )
    log.info(
        f'Successfully verified user can take book with ISBN {book1.isbn}')


def test_take_book_already_taken(user_1, user_2, setup_books):
    """Test that a user cannot take a book that is already taken."""
    _, book2, _ = setup_books
    log.info(
        f'User tries to take an already taken book with {book2.isbn} isbn')
    user_1.take_book(book2.isbn)
    log.info(f'User 2 tries to take already taken book with {book2.isbn} isbn')
    assert user_2.take_book(book2.isbn) is False, (
        f'Failed to prevent User 2 from taking the book with ISBN '
        f'{book2.isbn} '
        'that is already taken by User 1'
    )
    log.info(
        'Successfully verified user cannot take already taken book with ISBN '
        f'{book2.isbn}')


def test_reserve_book_positive(user_1, setup_books, c_book):
    """Test that a user can successfully reserve a book."""
    *_, book3 = setup_books
    log.info(f'User tries to reserve book with c {book3.isbn} isbn')
    assert user_1.reserve_book(book3.isbn), ('Failed to reserve the book with'
                                             f' ISBN {book3.isbn}')
    assert book3.isbn in c_book.reserved_books, (
        f'Book with ISBN {book3.isbn} is not in the reserved books list'
    )
    log.info(
        f'Successfully verified user can reserve book with ISBN {book3.isbn}'
        ' isbn')


def test_reserve_book_already_reserved(user_1, user_2, setup_books):
    """Test that a user cannot reserve a book."""
    *_, book3 = setup_books
    log.info(
        f'User tries to take an already reserved book with {book3.isbn} isbn')
    user_1.reserve_book(book3.isbn)
    log.info(
        f'User 2 tries to reserve already reserved book with'
        f' {book3.isbn} isbn')
    assert user_2.reserve_book(book3.isbn) is False, (
        f'Failed to prevent reserving a book with ISBN {book3.isbn} that is'
        ' already reserved')
    log.info(
        'Successfully verified user cannot reserve already reserved book '
        f'with ISBN {book3.isbn} ')


def test_return_book_positive(user_1, setup_books, c_book):
    """Test that a user can successfully return a book."""
    book1, *_ = setup_books
    log.info(f'User tries to return book with {book1.isbn} isbn')
    user_1.take_book(book1.isbn)
    assert user_1.return_book(book1.isbn), (
        f'Failed to return the book with ISBN {book1.isbn}'
    )
    assert {book1.isbn} not in c_book.taken_books, (
        f'Book with ISBN {book1.isbn} should not be in the list of taken books'
        ' after return')
    log.info('Successfully verified user can return book with ISBN 134527')


def test_return_book_not_taken(user_2, setup_books):
    """Test that a user cannot return a book that was not taken."""
    book1, *_ = setup_books
    log.info(f'User tries to return a not taken book with {book1.isbn} isbn')
    assert user_2.return_book(book1.isbn) is False, (
        'User was able to return a book with ISBN 134527 that was not taken'
    )
    log.info(
        'Successfully verified user cannot return a book that was not'
        f' taken with ISBN {book1.isbn}')


def test_release_book_positive(user_1, setup_books, c_book):
    """Test that a user can successfully release a reserved book."""
    _, book2, _ = setup_books
    log.info(f'User tries to release book with {book2.isbn} isbn')
    user_1.reserve_book(book2.isbn)
    assert user_1.release_book(book2.isbn), (
        f'Failed to release the book with ISBN {book2.isbn}')
    assert book2.isbn not in c_book.reserved_books, (
        f'Book with ISBN {book2.isbn} should not be in the list of '
        'taken books after return')
    log.info(
        'Successfully verified user can release reserved book with ISBN '
        f' {book2.isbn}')


def test_release_book_not_reserved(user_2, setup_books):
    """Test that a user cannot release a book that was not reserved."""
    *_, book3 = setup_books
    log.info(
        f'User tries to release a not reserved book with {book3.isbn} isbn')
    assert user_2.release_book(book3.isbn) is False, (
        f'User was able to release a book with ISBN {book3.isbn} that was not '
        'reserved'
    )
    log.info(
        'Successfully verified user cannot release a book that was not'
        f' reserved with ISBN {book3.isbn}')


def test_take_invalid_book(user_1):
    """Test that a user cannot take a book that does not exist."""
    log.info(
        f'User tries to take a non-existent book with {INCORRECT_ISBN} isbn')
    assert user_1.take_book(INCORRECT_ISBN) is False, (
        'fUser was able to take a book with ISBN {INCORRECT_ISBN} that does '
        'not exist'
    )
    log.info(
        'Successfully verified user cannot take a non-existent book with'
        f' ISBN {INCORRECT_ISBN}')


def test_reserve_invalid_book(user_1):
    """Test that a user cannot reserve a book that does not exist."""
    log.info(
        f'User tries to reserve a non-existent book with {INCORRECT_ISBN} '
        f'isbn')
    assert user_1.reserve_book(INCORRECT_ISBN) is False, (
        f'User was able to reserve a book with ISBN {INCORRECT_ISBN}'
        f' that does not exist')
    log.info(
        'Successfully verified user cannot reserve a non-existent book with'
        f' ISBN  {INCORRECT_ISBN}')


def test_return_invalid_book(user_1, ):
    """Test that a user cannot return a book that does not exist."""
    log.info(
        'User tries to return a non-existent book with {INCORRECT_ISBN} isbn')
    assert user_1.return_book(INCORRECT_ISBN) is False, (
        f'User was able to return a book with ISBN {INCORRECT_ISBN} '
        f'that does not exist'
    )
    log.info(
        'Successfully verified user can not return a non-existent book with '
        f'ISBN {INCORRECT_ISBN}')


def test_release_invalid_book(user_1):
    """Test that a user cannot release a book that does not exist."""

    log.info(
        'User tries to release a non-existent book with {INCORRECT_ISBN} isbn')
    assert user_1.release_book(INCORRECT_ISBN) is False, (
        f'User was able to release a book with ISBN {INCORRECT_ISBN}'
        f' that does not exist'
    )
    log.info(
        'Successfully verified user cannot release a non-existent book with '
        f'ISBN {INCORRECT_ISBN}')
