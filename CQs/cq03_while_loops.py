"""CQ03 While Loops"""

__author__ = "730740674"


def num_instances(phrase: str, search_char: str) -> int:
    """function to count number of instances of letter in a phrase"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count  # returns count (int) of letter in phrase
