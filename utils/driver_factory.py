from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config.config_reader import get_config


def get_driver(headless=True):
    options = Options()

    # Headless mode (for CI)
    if headless:
        options.add_argument("--headless=new")

    # Stability flags (VERY important for CI)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Create driver with WebDriver Manager
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Implicit wait from config
    driver.implicitly_wait(
        int(get_config("environment", "timeout"))
    )

    return driver