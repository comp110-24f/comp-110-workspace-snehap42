"""EX04 - list Utility Functions"""

__author__ = "730740674"


def all(list_int: list[int], int_check: int) -> bool:
    """Function to check if all list items match integer"""
    if len(list_int) == 0:
        return False  # returns False for an empty list
    idx: int = 0
    while idx < len(list_int):
        if int_check != list_int[idx]:
            return False  # returns False for any unmatching
        idx += 1
    return True  # branch for if all integers match


def max(input: list[int]) -> int:
    """Function to find the max integer in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")  # empty list path
    idx: int = 1
    max_int: int = input[0]
    while idx < len(input):
        if input[idx] > max_int:  # compares current max to next list element
            max_int = input[idx]
        idx += 1
    return max_int  # returns maximum


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Function to check for deep equality of two lists"""
    if len(list_1) != len(list_2):
        return False  # path for two lists of unequal length
    idx: int = 0
    while idx < len(list_1):
        if list_1[idx] != list_2[idx]:
            return False  # if one element of the list doesn't match at the index
        idx += 1
    return True  # all elements match at all indices


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Function to append list to another"""
    idx: int = 0
    while idx < len(list_2):
        list_1.append(list_2[idx])  # Append element at index of list_2
        idx += 1
    print(list_1)
