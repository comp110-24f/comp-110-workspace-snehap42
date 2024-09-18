"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730740674"


def input_word() -> str:
    """function to take input word that is 5 letters and exits if not"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word  # returns a five letter word from local variable word


def input_letter() -> str:
    """function to take input letter that is 1 letter and exits if not"""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter  # returns a single character from local variable


def contains_char(word: str, letter: str) -> None:
    """function to check if letter matches at each index in word and keeps count"""
    count = 0
    print("Searching for " + letter + " in " + word)
    if letter == word[0]:
        print(letter + " found at index 0")
        count = count + 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


# checking each letter and noting down instances with a final print
# of how many found


def main() -> None:
    """main function to centralize other functions"""
    contains_char(
        word=input_word(), letter=input_letter()
    )  # keeps the other functions in a main function


if __name__ == "__main__":
    main()  # keeps main function for library and will call the function
