from typing import Tuple
from math import floor


def division(dividend: int, divisor: int) -> Tuple[int, int]:
    quotient = floor(dividend / divisor)
    remainder = dividend % divisor
    return quotient, remainder
