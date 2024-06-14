"""Homework12_1: OOP. Writing and implementing programs."""


# Task_1 Library

class Book:
    """Initialize book objects"""
    taken_books = []
    reserved_books = []
    books = {}

    def __init__(self, name=None, isbn=None, pages=None, author=None):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.pages = pages
        self.books.update({self.isbn: {'name': self.name,
                                       'author': self.author,
                                       'pages': self.pages}})


class User(Book):
    """Initialize user objects"""
    users_books = {}

    def __init__(self, user_id):
        """Initializes the User objects"""
        self.user_id = user_id
        super().__init__()

    def update_user_book_status(self, isbn):
        """The method updates the status of the book."""
        if not self.users_books.get(self.user_id):
            self.users_books[self.user_id] = [isbn]
        else:
            if isbn in self.users_books[self.user_id]:
                print(
                    f'The book with ISBN: {isbn} is in progress '
                    f'for user {self.user_id}')
            self.users_books[self.user_id].append(isbn)

    def take_book(self, isbn):
        """The method checks the status of the book and the possibility
        of borrowing it from the library."""
        if isbn in self.books:
            if (isbn not in self.reserved_books and isbn not in
                    self.taken_books):
                self.taken_books.append(isbn)
                self.update_user_book_status(isbn)
                return True

            print(f'book with {isbn} is unavailable, '
                  f'additional info: {self.books.get(isbn)}')
            return False

        print(f'we do not have book with id "{isbn}"')
        return False

    def reserve_book(self, isbn):
        """The method checks the status of the book and the possibility
           of reserving it in the library."""
        if isbn in self.books:
            if (isbn not in self.reserved_books and isbn not
                    in self.taken_books):
                self.reserved_books.append(isbn)
                self.update_user_book_status(isbn)
                return True

            print(f'book with {isbn} unavailable, '
                  f'additional info: {self.books.get(isbn)}')
            return False

        print(f'we do not have book with id "{isbn}"')
        return False

    def return_book(self, isbn):
        """The method checks the status of the book and the possibility
               of returning it to the library """
        if isbn in self.books:
            if (isbn in self.taken_books and isbn in
                    self.users_books[self.user_id]):
                self.taken_books.remove(isbn)
                self.users_books[self.user_id].remove(isbn)
                return True

            print(
                f'The book with {isbn} was not taken '
                f'by user with id {self.user_id}',
                f'additional info: {self.books.get(isbn)}')
            return False
        print(f'you can not return book with id "{isbn}"')
        return False

    def release_book(self, isbn):
        """The method checks if the book reserved """
        if isbn in self.books:
            if (isbn in self.reserved_books
                    and isbn in self.users_books[self.user_id]):
                self.reserved_books.remove(isbn)
                self.users_books[self.user_id].remove(isbn)
                return True

            print(
                f'The book with {isbn} was not reserved '
                f'by user with id {self.user_id}'
                f'additional info: {self.books.get(isbn)}')
            return False

        print(
            f'you can not release book with id "{isbn}", '
            f'we do not have it')
        return False


book1 = Book("Learning Python", "134527", 1200,
             "Mark Lutz")
book2 = Book("Learn Python 3 the Hard Way", "234569", 1000,
             "Zed A. Shaw")
book3 = Book("Think Python", "239874",
             900, "Allen Downey ")

user_1 = User('user_id_1')
assert user_1.take_book('134527')
assert user_1.take_book('234569')
assert user_1.reserve_book('234569') is False
assert user_1.return_book('134527')
assert user_1.release_book('134527') is False
assert user_1.return_book('234569')

user_2 = User('user_id_2')
assert user_2.take_book('134527')
assert user_2.return_book('312312') is False
assert user_2.return_book('134527')

assert User.users_books.get('user_id_1') == []
assert User.users_books.get('user_id_2') == []
