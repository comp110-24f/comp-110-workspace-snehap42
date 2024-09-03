"""Ex01 Tea Party assignment: showing plans for tea party guest number"""

__author__ = "730740674"


def main_planner(guests: int) -> None:
    """function to be entrypoint of program and create output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


def tea_bags(people: int) -> int:
    """function to find number of tea bags based on people coming"""
    return 2 * people


def treats(people: int) -> int:
    """function to find number of treats based on  guest number"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """function to find cost of tea bags and treats combined"""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
