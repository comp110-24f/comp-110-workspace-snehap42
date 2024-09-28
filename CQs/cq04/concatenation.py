"""CQ04 Concatenation"""

__author__ = "730740674"


def concat(strinput1: str, strinput2: str) -> str:
    """adds two strings together"""
    return strinput1 + strinput2  # returns the result of adding two strings


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
