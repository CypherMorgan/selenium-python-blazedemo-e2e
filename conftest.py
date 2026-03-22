import pytest
import pytest_html
from utils.driver_factory import get_driver
from utils.logger import get_logger
from utils.screenshot import take_screenshot
from config.config_reader import get_config


@pytest.fixture(scope="function")
def driver():

    driver = get_driver()

    base_url = get_config("environment", "base_url")
    driver.get(base_url)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

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

            extra.append(pytest_html.extras.html(html))

        report.extra = extra

logger = get_logger("TestRunner")


def pytest_runtest_setup(item):
    logger.info(f"TEST STARTED: {item.name}")


def pytest_runtest_teardown(item):
    logger.info(f"TEST FINISHED: {item.name}")

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)

@pytest.fixture
def driver(request):
    headless = request.config.getoption("--headless")
    driver = get_driver(headless=headless)
    yield driver
    driver.quit()