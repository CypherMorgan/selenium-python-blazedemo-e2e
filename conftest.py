import pytest
import pytest_html

from utils.driver_factory import get_driver
from utils.logger import get_logger
from utils.screenshot import take_screenshot
from config.config_reader import get_config

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
def driver(request):
    headless = request.config.getoption("--headless")
    browser = request.config.getoption("--browser")

    driver = get_driver(browser=browser, headless=headless)

    base_url = get_config("environment", "base_url")
    driver.get(base_url)

    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when == "call":
        driver = item.funcargs.get("driver")

        if report.failed and driver:
            screenshot_path = take_screenshot(driver, item.name)

            html = (
                f'<div><img src="../{screenshot_path}" '
                f'style="width:400px;height:200px;" '
                f'onclick="window.open(this.src)" '
                f'align="right"/></div>'
            )

            extras.append(pytest_html.extras.html(html))

    report.extras = extras

logger = get_logger("TestRunner")

def pytest_runtest_setup(item):
    logger.info(f"TEST STARTED: {item.name}")

def pytest_runtest_teardown(item):
    logger.info(f"TEST FINISHED: {item.name}")