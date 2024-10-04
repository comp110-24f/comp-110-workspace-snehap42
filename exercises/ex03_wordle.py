"""Ex 03: Wordle"""

__author__ = "730740674"


def input_guess(secret_word_len: int) -> str:
    """Asks for a guess from user and checks that it is the correct length"""
    while True:
        guess = input("Enter a " + str(secret_word_len) + " character word: ")
        if len(guess) == secret_word_len:
            return guess  # Correct length returns guess
        else:
            print(
                "That wasn't " + str(secret_word_len) + " chars! Try again:"
            )  # incorrect length another guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Looking for character in secret word"""
    assert len(char_guess) == 1
    idx_secret: int = 0
    while idx_secret < len(secret_word):
        if secret_word[idx_secret] == char_guess:
            return True  # returns character is in secret word
        else:
            idx_secret += 1
    return False  # returns character is not in secret word


def emojified(guess: str, secret: str) -> str:
    """Function creates emojis for letter being correct or in the right place"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    idx: int = 0
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX  # correct letter in correct space
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX  # correct letter incorrect space
        else:
            result += WHITE_BOX  # incorrect letter
        idx += 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn < 7:
        print("=== Turn " + str(turn) + "/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print("You won in " + str(turn) + "/6 turns!")
            return  # returns a success
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")  # returns a fail after loop


if __name__ == "__main__":
    main(secret="codes")
