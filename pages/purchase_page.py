from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config_reader import get_passenger_data


class PurchasePage(BasePage):

    NAME = (By.ID, "inputName")
    ADDRESS = (By.ID, "address")
    CITY = (By.ID, "city")
    STATE = (By.ID, "state")
    ZIP = (By.ID, "zipCode")
    CARD_NUMBER = (By.ID, "creditCardNumber")
    PURCHASE_BTN = (By.CSS_SELECTOR, "input[type='submit']")

    def fill_passenger_details(self, passenger):

        self.logger.info(f"Entering passenger details for {passenger['name']}")

        self.type(self.NAME, passenger["name"])
        self.type(self.ADDRESS, passenger["address"])
        self.type(self.CITY, passenger["city"])
        self.type(self.STATE, passenger["state"])
        self.type(self.ZIP, passenger["zip"])
        self.type(self.CARD_NUMBER, passenger["card"])

        self.logger.info("Passenger details entered successfully")

    def complete_purchase(self):
        
        self.logger.info("Submitting purchase")

        self.click(self.PURCHASE_BTN)