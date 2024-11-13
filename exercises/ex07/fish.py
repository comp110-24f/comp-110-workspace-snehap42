"""File to define Fish class."""

__author__ = "730740674"


class Fish:
    """Class for Fish."""

    age: int

    def __init__(self):
        """Creates Fish."""
        self.age = 0
        return None  # sets new fish

    def one_day(self):
        """Fn increases one day."""
        self.age += 1
        return None  # increases age
