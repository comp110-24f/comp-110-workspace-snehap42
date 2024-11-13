"""File to define River class."""

__author__ = "730740674"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Class for river."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def remove_fish(self, amount: int) -> None:
        """Function to remove fish."""
        while amount > 0 and self.fish:
            self.fish.pop(0)
            amount -= 1  # decrease amount to add

    def check_ages(self):
        """Function to check bear and fish ages."""
        surviving_f_list: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_f_list.append(fish)
        self.fish = surviving_f_list
        surviving_bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bear_list.append(bear)
        self.bears = surviving_bear_list
        return None  # checks and adds to survivors

    def bears_eating(self):
        """Function to remove eaten fish."""
        for bear in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                bear.eat(3)
        return None  # removes fish and adds to bear

    def check_hunger(self):
        """Function to remove starved bears."""
        surviving_bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bear_list.append(bear)
        self.bears = surviving_bear_list
        return None  # removes starved bears with new list

    def repopulate_fish(self):
        """Fn to add fish created."""
        added_fish = (len(self.fish) // 2) * 4
        while added_fish > 0:
            self.fish.append(Fish())  # Adds new fish
            added_fish -= 1
        return None

    def repopulate_bears(self):
        """Fn to add bears reproduced."""
        added_bears = len(self.bears) // 2
        while added_bears > 0:
            self.bears.append(Bear())  # Adds bear
            added_bears -= 1
        return None

    def view_river(self):
        """Function to see river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None  # prints all

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Increases days for a week."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None  # called 7 times the one_river_day
