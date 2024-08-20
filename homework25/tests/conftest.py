from datetime import datetime
from pathlib import Path
import logging
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Add CLI option for headless mode."""
    parser.addoption(
        "--headless",
        action="store",
        default=False,
        help="Set headless mode"
    )


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Configure pytest to generate an HTML report."""
    now = datetime.now()
    reports_dir = Path('test_reports')
    reports_dir.mkdir(parents=True, exist_ok=True)
    report = reports_dir / f"Test_report_{now.strftime('%Y-%m-%d %H:%M:%S')}.html"
    logging.debug(f"Creating test report: {report}")
    config.option.htmlpath = report
    config.option.self_contained_html = True


@pytest.fixture
def driver(request):
    """Initialize and yield a Chrome WebDriver instance."""
    headless = request.config.getoption("--headless")
    headless = headless.lower() == 'true' if isinstance(headless, str) else headless
    _options = webdriver.ChromeOptions()
    if headless:
        _options.add_argument("--headless")
    _options.add_argument("--window-size=1920,1080")
    logging.info(f"Start Chrome Webdriver: options: {_options}")
    web_driver = webdriver.Chrome(options=_options)
    yield web_driver
    web_driver.close()
    web_driver.quit()
