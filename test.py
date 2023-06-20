import pytest

from app import division


class TestDivision:
    def test_division_normal(self):
        assert division(55, 9) == (6, 2)

    def test_division_divided_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            division(55, 0)
