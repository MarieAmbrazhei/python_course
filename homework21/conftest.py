"""This module contains shared fixtures for pytest that can be used across
multiple test files."""

from typing import Tuple
import pytest
from pymar_logging import logger as log
from constants import LOG_LEVELS
from homework12.homework12_2 import Bank, Deposit
from homework12.homework12_1 import User, Book


def pytest_addoption(parser):
    """Describes that the function adds a command-line option to set the
        HTML log level."""
    parser.addoption(
        "--log_cli_level",
        action="store",
        default="INFO",
        help="Set the logging level for CLI"
    )
    parser.addini("log_cli", default=True, help="Enable CLI logging")
    parser.addini("log_cli_level", default="INFO",
                  help="Set log level for CLI")
    parser.addini("log_file_level", default="DEBUG",
                  help="Set log level for log file")


def pytest_configure(config):
    """Describes that the function configures logging based on the
    command-line option"""
    if config.pluginmanager.hasplugin("html"):
        htmlpath = config.getoption("--html") or "report.html"
        config.option.htmlpath = htmlpath
        config.option.self_contained_html = True

    config.option.log_cli = config.getini("log_cli")
    config.option.log_file_level = config.getini("log_file_level")

    # Set the CLI log level
    log_cli_level = config.getoption("--log_cli_level").upper()
    if log_cli_level in LOG_LEVELS:
        config.option.log_cli_level = log_cli_level
        log.setLevel(LOG_LEVELS[log_cli_level])
    else:
        raise ValueError(f"Invalid log level: {log_cli_level}")


@pytest.fixture
def initial_bank():
    """
    Creates and deletes banks
    """
    bank_1 = Bank(10)

    yield bank_1
    del bank_1


@pytest.fixture
def deposit_1():
    """
    Creates and deletes deposits
    """
    dep_1 = Deposit(10000, 2
                    )
    yield dep_1
    del dep_1


@pytest.fixture
def deposit_2():
    """Creates and deletes deposits"""
    dep_2 = Deposit(15000, 2)

    yield dep_2
    del dep_2


@pytest.fixture
def setup_books() -> Tuple[Book, ...]:
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


@pytest.fixture
def c_book() -> Book:
    """
    Return Book object
    """
    return Book()
