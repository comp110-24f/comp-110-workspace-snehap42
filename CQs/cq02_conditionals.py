"""CQ02: Guess a number"""

__author__ = "730740674"


def guess_a_number() -> None:
    "Function to guess a number with conditionals+input+variables"
    secret: int = 7
    x: int = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x == secret:
        print("You got it!")
    if x < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif x > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
