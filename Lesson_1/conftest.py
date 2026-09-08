import pytest
from calculator import Calculator

@pytest.fixture(scope="module")
def create_calculator():
    return Calculator()