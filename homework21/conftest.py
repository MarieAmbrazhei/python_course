from pymar_logging import logger as log
from constants import LOG_LEVELS


def pytest_addoption(parser):
    """Describes that the function adds a command-line option to set the
     HTML log level."""
    parser.addoption(
        "--html-log-level",
        action="store",
        default="INFO",
        help="Set the logging level for html report"
    )


def pytest_configure(config):
    """Describes that the function configures logging based on the
    command-line option"""
    log_level = config.getoption("--html-log-level").upper()
    if log_level_numeric := LOG_LEVELS.get(log_level):
        log.setLevel(log_level_numeric)
