"""EX06: Dictionary Utility"""

__author__ = "730740674"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Function to switch keys and values"""
    inverted_dict: dict[str, str] = {}
    for key in input_dict:
        value = input_dict[key]
        if value in inverted_dict:
            raise KeyError(
                "Error: Duplicate Keys"
            )  # error for two of the same key in new dict
        inverted_dict[value] = key
    return inverted_dict  # returns new dict inverted


def favorite_color(input_dict: dict[str, str]) -> str:
    """Function to find most popular color"""
    color_count_dict: dict[str, int] = {}
    for name in input_dict:
        color = input_dict[name]
        if color in color_count_dict:
            color_count_dict[color] += 1
        else:
            color_count_dict[color] = 1

    favorite_color = ""
    max_count = 0  # sets max for comparison

    for name in input_dict:
        color = input_dict[name]
        count = color_count_dict[color]
        if color_count_dict[color] > max_count:
            favorite_color = color
            max_count = color_count_dict[color]
        elif count == max_count and favorite_color == "":
            favorite_color = color  # returns tied color
    return favorite_color  # returns color


def count(input_list: list[str]) -> dict[str, int]:
    """Function to keep track of item count in dict"""
    count_dict: dict[str, int] = {}
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict  # returns frequency


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Function to organize the items in a list alphabetically"""
    alphabetized_dict: dict[str, list[str]] = {}

    for word in input_list:
        first_letter = word[0].lower()

        if first_letter in alphabetized_dict:
            alphabetized_dict[first_letter].append(word)  # if letter in list

        else:
            alphabetized_dict[first_letter] = [word]  # if letter not in
    return alphabetized_dict  # returns new dict


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Function to add attendance of a day with names to a growing dict"""
    if day in input_dict:
        if student in input_dict[day]:
            return None
        input_dict[day].append(student)  # adds student
    else:
        input_dict[day] = [student]  # creates day
    return None
