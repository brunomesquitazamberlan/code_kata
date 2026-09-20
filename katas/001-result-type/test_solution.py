import pytest

from solution import divide


def test_divide_returns_ok_for_valid_division():
    result = divide(10, 2)

    assert result.is_ok() is True
    assert result.unwrap() == 5.0


def test_divide_returns_ok_when_result_is_zero():
    result = divide(0, 10)

    assert result.is_ok() is True
    assert result.unwrap() == 0.0


def test_divide_returns_err_when_dividing_by_zero():
    result = divide(10, 0)

    assert result.is_ok() is False


def test_unwrap_err_raises_runtime_error():
    result = divide(10, 0)

    with pytest.raises(RuntimeError):
        result.unwrap()
