"""File to define Bear class."""

__author__ = "730740674"


class Bear:
    """Class for Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """New Bear."""
        self.age = 0
        self.hunger_score = 0
        return None  # constructor returns none

    def one_day(self):
        """Increases for one day."""
        self.age += 1
        self.hunger_score -= 1
        return None  # age and hunger increase

    def eat(self, num_fish: int):
        """Fn for eating fish."""
        self.hunger_score += num_fish  # hunger increases by fish
        return None
