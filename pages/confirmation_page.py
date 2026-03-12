from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ConfirmationPage(BasePage):

    CONFIRMATION_HEADER = (By.TAG_NAME, "h1")

    def get_confirmation_message(self):

        message = self.get_text(self.CONFIRMATION_HEADER)

        self.logger.info(f"Booking confirmation received: {message}")

        return message