from pages.home_page import HomePage


def test_search_flights(driver):

    home = HomePage(driver)

    home.search_flights("Boston", "London")

    assert "Flights from Boston to London" in driver.page_source