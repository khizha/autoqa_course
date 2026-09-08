import pytest


def test_sum_positive_numbers(create_calculator):
    assert create_calculator.sum(2,4) == 6
    assert create_calculator.sum(2, 5) == 7
    assert create_calculator.sum(1, 8) == 9


@pytest.mark.xfail(strict=True, reason="Метод в процессе разработки") # декоратор делает так, чтобы тест провалился
def test_sum_negative_numbers(create_calculator):
    assert create_calculator.sum(-2,-4) == -6
    assert create_calculator.sum(-2, -5) == -7
    assert create_calculator.sum(-1, -8) == -9


@pytest.mark.skipif(condition="sys.version_info > (3, 8)", reason = "Python version is greater than 3.8")
def test_division(create_calculator):
    assert create_calculator.div(4, 2) == 2
    assert create_calculator.div(8, 2) == 4
    assert create_calculator.div(10, 5) == 2

def test_division_by_zero(create_calculator):
    with pytest.raises(ArithmeticError, match="by zero"):
        create_calculator.div(4, 0)