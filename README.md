# Selenium Python BlazeDemo E2E Automation

![Python](https://img.shields.io/badge/python-3.x-blue)
![Selenium](https://img.shields.io/badge/selenium-automation-green)
![PyTest](https://img.shields.io/badge/pytest-testing-orange)

End-to-end UI automation framework built using **Selenium, Python, and PyTest**.
The project automates a complete flight booking flow on **https://blazedemo.com/** using a clean **Page Object Model (POM)** architecture.

This repository demonstrates a realistic automation framework structure with logging, reporting, retry logic, and data-driven testing.

---

# Tech Stack

* Python
* Selenium WebDriver
* PyTest
* Page Object Model (POM)
* PyTest HTML Reporting
* PyTest xdist (parallel execution)
* PyTest rerunfailures (retry failed tests)

---

# Test Scenario

The automation covers the following end-to-end workflow:

1. Search for available flights
2. Select a flight
3. Enter passenger details
4. Complete the booking
5. Verify the booking confirmation message

---

# Framework Features

* Page Object Model architecture
* Explicit waits for stable test execution
* Config-driven test settings
* Data-driven testing with PyTest parametrize
* Automatic screenshots on test failure
* Screenshots embedded in HTML reports
* Structured logging for debugging
* Parallel test execution
* Automatic retry of flaky tests
* Clean modular framework structure

---

# Project Structure

```
selenium-python-blazedemo-e2e
│
├── config
│   ├── config.ini
│   └── config_reader.py
│
├── data
│   └── passengers.py
│
├── pages
│   ├── base_page.py
│   ├── home_page.py
│   ├── flights_page.py
│   ├── purchase_page.py
│   └── confirmation_page.py
│
├── tests
│   ├── test_flight_booking.py
│   ├── test_home_page.py
│   └── test_flight_search.py
│
├── utils
│   ├── driver_factory.py
│   ├── logger.py
│   └── screenshot.py
│
├── logs
├── reports
├── screenshots
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Data Driven Testing

Passenger test data is defined in:

```
data/passengers.py
```

The test uses **PyTest parametrize** to automatically execute the same test for multiple passengers.

Example dataset:

```
PASSENGERS = [
    {"name": "John Tester", ...},
    {"name": "Alice Walker", ...},
    {"name": "Michael Smith", ...}
]
```

PyTest automatically generates multiple test executions:

```
test_end_to_end_booking[John Tester]
test_end_to_end_booking[Alice Walker]
test_end_to_end_booking[Michael Smith]
```

---

# Installation

Clone the repository:

```
git clone https://github.com/CypherMorgan/selenium-python-blazedemo-e2e.git
cd selenium-python-blazedemo-e2e
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Running Tests

Run all tests:

```
pytest
```

Run with detailed output:

```
pytest -v
```

Run tests in parallel:

```
pytest -n auto
```

---

# Test Reports

After execution, the framework generates:

```
reports/report.html
```

The HTML report includes:

* Test execution results
* Pass / fail status
* Execution time
* Error stack traces
* Embedded failure screenshots

Open the report in your browser:

```
reports/report.html
```

---

# Logging

Execution logs are stored in:

```
logs/test.log
```

Logs include structured test steps such as:

```
HomePage | Searching flights: Boston -> London
FlightsPage | Selecting first available flight
PurchasePage | Filling passenger details
ConfirmationPage | Booking confirmation received
```

This helps debugging failed tests quickly.

---

# Failure Screenshots

When a test fails:

* A screenshot is automatically captured
* The image is saved in the **screenshots/** directory
* The screenshot is embedded in the **HTML report**

---

# Future Improvements

Potential enhancements for the framework:

* Data-driven testing using **CSV or Excel files**
* Allure reporting integration
* CI/CD pipeline using **GitHub Actions**
* Browser selection via command-line parameters
* Headless test execution support
* Test environment profiles (dev / staging / prod)

---

# Author

Automation framework created as a learning project while practicing **QA Automation using Selenium and Python**.
