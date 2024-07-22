"""
Unit tests for the Homework_12: library.
"""

import unittest
from homework12.homework12_1 import Book, User
from pymar_logger import logger as log


class TestLibrary(unittest.TestCase):
    """
    Test cases for the Library class deposit method.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        Book.taken_books = []
        Book.reserved_books = []
        Book.books = {}
        User.users_books = {}

        self.book1 = Book("Learning Python", "134527", 1200,
                          "Mark Lutz")
        self.book2 = Book("Learn Python 3 the Hard Way", "234569",
                          1000,
                          "Zed A. Shaw")
        self.book3 = Book("Think Python", "239874",
                          900, "Allen Downey ")

        self.user_1 = User('user_id_1')
        self.user_2 = User('user_id_2')

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.book1
        del self.book2
        del self.book3

        del self.user_1
        del self.user_2

    def test_take_book_positive(self):
        """Test taking a book that is available."""
        log.info(f'User tries to take book with {self.book1.isbn} isbn')
        self.assertTrue(self.user_1.take_book(self.book1.isbn))
        self.assertIn(self.book1.isbn, User.taken_books)
        log.info(
            f'Successfully verified: User took book with  {self.book1.isbn} isbn')

    def test_take_book_already_taken(self):
        """Test that a user cannot take a book that is already taken."""

        log.info(
            f'User tries to take an already taken book with {self.book2.isbn} isbn')
        self.user_1.take_book(self.book2.isbn)
        self.assertFalse(self.user_2.take_book(self.book2.isbn))
        log.info(
            f'Successfully verified: book with {self.book2.isbn} is unavailable,'
            f' additional info: {Book.books.get(self.book2.isbn)}')

    def test_reserve_book_positive(self):
        """Test that a user can successfully reserve a book."""
        log.info(f'User tries to  reserve  book with {self.book1.isbn} isbn')
        self.assertTrue(self.user_1.reserve_book(self.book1.isbn))
        self.assertIn(self.book1.isbn, User.reserved_books)
        log.info(
            f'Successfully verified: User reserved book with  {self.book1.isbn} '
            f'isbn')

    def test_reserve_book_already_reserved(self):
        """Test that a user cannot reserve a book."""
        log.info(
            'User tries to  reserve  an already reserved  book with'
            f' {self.book3.isbn} isbn')
        self.user_1.reserve_book(self.book3.isbn)
        self.assertFalse(self.user_2.reserve_book(self.book3.isbn))
        log.info(
            f'Successfully verified: book with {self.book3.isbn} unavailable,'
            f' additional info: {Book.books.get(self.book3.isbn)}')

    def test_return_not_taken_book_positive(self):
        """Test that a user can successfully return a book."""
        # isbn = '134527'
        log.info(f'User tries to  return book with {self.book1.isbn} isbn')
        self.assertFalse(self.user_1.return_book(self.book1.isbn))
        self.assertNotIn(self.book1.isbn, User.taken_books)
        log.info(f'Successfully verified: User can not return book with  '
                 f'{self.book1.isbn} isbn')

    def test_return_book_not_taken(self):
        """Test that a user cannot return a book that was not taken."""
        log.info(
            f'User tries to return a not taken book with {self.book1.isbn} isbn')
        self.assertFalse(self.user_2.return_book(self.book1.isbn))
        log.info(
            f'Successfully verified: User can not return book with  {self.book1.isbn} '
            f'isbn')

    def test_release_book_positive(self):
        """Test that a user can successfully release a reserved book."""
        log.info(f'User tries to release book with {self.book1.isbn} isbn')
        self.user_1.reserve_book(self.book1.isbn)
        self.assertTrue(self.user_1.release_book(self.book1.isbn))
        self.assertNotIn(self.book1.isbn, User.reserved_books)
        log.info(
            f'Successfully verified: User can release book with  {self.book1.isbn} '
            f'isbn')

    def test_release_book_not_reserved(self):
        """Test that a user cannot release a book that was not reserved."""
        log.info(
            f'User tries to release a not reserved book with {self.book1.isbn} isbn')
        self.assertFalse(self.user_2.release_book(self.book1.isbn))
        log.info(
            f'Successfully verified: User can not release book with  {self.book1.isbn} '
            f'isbn')

    def test_take_invalid_book(self):
        """Test that a user cannot take a book that does not exist."""
        isbn = '111111'
        log.info('User tries to take a not existent book with 111111 isbn')
        self.assertFalse(self.user_1.take_book('111111'))
        log.info(
            f'Successfully verified: User can not take book with  {isbn} '
            f'isbn')

    def test_reserve_invalid_book(self):
        """Test that a user cannot reserve a book that does not exist."""
        isbn = '111111'
        log.info('User tries to reserve a not existent book with 111111 isbn')
        self.assertFalse(self.user_1.reserve_book('111111'))
        log.info(
            f'Successfully verified: User can not reserve book with  {isbn} '
            f'isbn')

    def test_return_invalid_book(self):
        """Test that a user cannot return a book that does not exist."""
        isbn = '111111'
        log.info('User tries to return a not existent book with 111111 isbn')
        self.assertFalse(self.user_1.return_book('111111'))
        log.info(
            f'Successfully verified: User can not return book with  {isbn} '
            f'isbn')

    def test_release_invalid_book(self):
        """Test that a user cannot release a book that does not exist."""
        isbn = '111111'
        log.info('User tries to release a not existent book with 111111 isbn')
        self.assertFalse(self.user_1.release_book('111111'))
        log.info(
            f'Successfully verified: User can not release book with  {isbn} '
            f'isbn')


if __name__ == '__main__':
    unittest.main()
