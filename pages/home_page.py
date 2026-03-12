from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    FROM_PORT = (By.NAME, "fromPort")
    TO_PORT = (By.NAME, "toPort")
    FIND_FLIGHTS_BTN = (By.CSS_SELECTOR, "input[type='submit']")

    def search_flights(self, from_city, to_city):

        self.logger.info(f"Searching flights: {from_city} -> {to_city}")

        from_dropdown = self.wait.until(
            lambda d: d.find_element(*self.FROM_PORT)
        )
        from_dropdown.send_keys(from_city)

        to_dropdown = self.driver.find_element(*self.TO_PORT)
        to_dropdown.send_keys(to_city)

        self.logger.info("Clicking 'Find Flights'")

        self.click(self.FIND_FLIGHTS_BTN)