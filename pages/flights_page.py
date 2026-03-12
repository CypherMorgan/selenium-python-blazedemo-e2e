from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FlightsPage(BasePage):

    CHOOSE_FLIGHT_BTN = (By.CSS_SELECTOR, "table tbody tr:first-child input")

    def choose_first_flight(self):
        try:
            self.click(self.CHOOSE_FLIGHT_BTN)
        except Exception as e:
            print(f"Could not select flight: {e}")
            raise