import pytest
from simple_math import SimpleMath


@pytest.fixture
def simple_math():
    return SimpleMath()