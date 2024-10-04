"""Mutating functions."""

__author__ = "730740674"


def manual_append(append_list: list[int], append_int: int) -> None:
    """function to append integer to list"""
    append_list.append(append_int)  # adds int to end of list


def double(double_list: list[int]) -> None:
    """doubles each element in list by 2"""
    idx: int = 0
    while idx < len(double_list):
        double_list[idx] *= 2  # doubles each value in list
        idx += 1  # increases index for loop


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
