"""CQ07: Unit Test"""

__author__ = "730740674"

from CQs.cq07.find_max import (
    find_and_remove_max,
)  # imports function from find max module


def test_find_and_remove_max_1() -> None:
    "Function for use case and value"
    input_list = [2, 4, 6]
    assert find_and_remove_max(input_list) == 6  # max value is 6


def test_find_and_remove_max_2() -> None:
    "Function for use case and list"
    input_list = [3, 5, 5, 1, 5]
    find_and_remove_max(input_list)
    assert input_list == [3, 1]  # list does not have 5


def test_find_and_remove_max_3() -> None:
    "Function for edge case"
    input_list = []
    max_value = find_and_remove_max(input_list)
    assert max_value == -1  # value is -1
