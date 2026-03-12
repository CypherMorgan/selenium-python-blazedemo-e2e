import os
from datetime import datetime


def take_screenshot(driver, test_name):

    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"{test_name}_{timestamp}.png"

    path = os.path.join(screenshots_dir, file_name)

    driver.save_screenshot(path)

    return path