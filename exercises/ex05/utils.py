"""EX05: Utils"""

__author__ = "730740674"


def only_evens(input: list[int]) -> list:
    """function to return only evens in a list"""
    idx: int = 0
    evens_list: list[int] = []
    while idx < len(input):
        if input[idx] % 2 == 0:
            evens_list.append(input[idx])
        idx += 1
    return evens_list  # returns evens


def sub(input: list[int], start_index: int, end_index: int) -> list[int]:
    """function to return subset of a list"""
    sub_list: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index > len(input):
        end_index = len(input)
    if len(input) == 0 or start_index >= len(input) or end_index <= 0:
        return sub_list  # returns empty list for empty, too much start or end
    for idx in range(start_index, end_index):
        sub_list.append(input[idx])
    return sub_list  # returns some of list


def add_at_index(input_list: list[int], input_int: int, input_index: int) -> None:
    """function to add new int at index"""
    if input_index < 0 or input_index > len(input_list):
        raise IndexError("Index is out of bounds for the input list")
    input_list.append(0)  # adds space
    for idx in range(len(input_list) - 1, input_index - 1, -1):
        input_list[idx] = input_list[idx - 1]  # shifts value to index to the right
    input_list[input_index] = input_int  # puts new value in wanted index
