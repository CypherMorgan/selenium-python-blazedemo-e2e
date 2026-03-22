from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(browser="chrome", headless=True):

    if browser.lower() == "chrome":
        options = ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif browser.lower() == "firefox":
        options = FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)

    else:
        raise Exception(f"Browser '{browser}' not supported")

    return driver