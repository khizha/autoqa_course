import pytest


@pytest.fixture
def booking_data():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-11-10",
            "checkout": "2026-11-15"
        },
        "additionalneeds": "Breakfast"
    }