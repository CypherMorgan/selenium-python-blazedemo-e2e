import pytest

from pages.home_page import HomePage
from pages.flights_page import FlightsPage
from pages.purchase_page import PurchasePage
from pages.confirmation_page import ConfirmationPage

from data.passengers import PASSENGERS


@pytest.mark.parametrize(
    "passenger",
    PASSENGERS,
    ids=[p["name"] for p in PASSENGERS]
)
def test_end_to_end_booking(driver, passenger):

    home = HomePage(driver)
    flights = FlightsPage(driver)
    purchase = PurchasePage(driver)
    confirmation = ConfirmationPage(driver)

    home.search_flights("Boston", "London")

    flights.choose_first_flight()

    purchase.fill_passenger_details(passenger)

    purchase.complete_purchase()

    message = confirmation.get_confirmation_message()

    assert "Thank you for your purchase today!" in message