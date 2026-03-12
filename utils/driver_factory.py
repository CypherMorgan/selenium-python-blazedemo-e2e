from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.config_reader import get_config


def get_driver():

    browser = get_config("environment", "browser")

    if browser.lower() == "chrome":

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        driver.implicitly_wait(
            int(get_config("environment", "timeout"))
        )

        return driver

    else:
        raise Exception("Browser not supported")