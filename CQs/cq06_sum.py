"""Summing the elements of a list using different loops"""

__author__ = "730740674"


def w_sum(vals: list[float]) -> float:
    """function to sum with a while loop"""
    sum: float = 0.0
    idx: int = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum  # returns sum as float from while loop


def f_sum(vals: list[float]) -> float:
    """function to sum with a for loop"""
    sum: float = 0.0
    for val in vals:
        sum += val
    return sum  # returns sum as float from for loop


def f_range_sum(vals: list[float]) -> float:
    """function to sum with a for loop and range"""
    sum: float = 0.0
    idx: int = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum  # returns sum as float from for loop and range
