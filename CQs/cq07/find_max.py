"""CQ07: Find Max"""

__author__ = "730740674"


def find_and_remove_max(input: list[int]) -> int:
    """Function to find and remove max"""
    if len(input) == 0:
        return -1
    idx: int = 0
    max: int = input[0]
    while idx < len(input):
        if input[idx] > max:
            max = input[idx]
        idx += 1
    idx = 0
    while idx < len(input):
        if max == input[idx]:
            input.pop(idx)
        else:
            idx += 1  # increases if not removed
    return max  # returns max value
