from random import choice
from english_words import get_english_words_set
from re import findall


def main():
    tries = []
    tried_letter = []
    words = list(get_english_words_set(["web2"], lower=True))

    def chosen_word(difficulty: list):
        """Choose a random word based on the difficulty chosen them return a list with
        the enumerated word, the string with underscores in lenght of the word and 
        marker of correct guesses.
        """
        word = choice(difficulty)
        return [list(enumerate(word)), "_" * len(word)]

    def choosing_difficulty():
        """Choose a difficulty between 1(Easy), 2(Medium) and 3 (Hard) then return an
        array with words based in which difficulty was chosen.
        """
        while True:
            try:
                difficulty = int(
                    input(
                        "Please choose a difficulty between 1(easy), 2(medium) and 3(hard): "
                    )
                )
            except ValueError:
                print("Please only choose 1, 2 or 3.\n")
                return choosing_difficulty()
            match difficulty:
                case 1:
                    print("You have choosen the easy difficulty.")
                    return [w for w in words if len(w) > 4 and len(w) <= 9]
                case 2:
                    print("You have choosen the medium difficulty.")
                    return [w for w in words if len(w) > 3 and len(w) <= 6]
                case 3:
                    print("You have choosen the hard difficulty.")
                    return [w for w in words if len(w) == 3]
                case _:
                    print("You didn't choose a valid difficulty. Please try again.")

    def verified_input():
        """Ask for a letter and return that letter if the input is valid."""
        while True:
            letter: str = input("\nPlease choose a letter: ")
            if (
                letter in findall(r"[A-z]", letter.strip())
                and letter not in tried_letter
            ):
                tried_letter.append(letter)
                return letter.lower()
            elif not letter.isalpha():
                print("\nPlease choose a letter better a and Z.")
            elif len(letter) != 1:
                print("\nPlease choose only 1(one) letter.")
            elif letter in tried_letter:
                print(
                    "\nYou have already tried this letter, please choose a different letter."
                )
            else:
                print("\nSorry, that wasn't a valid input")

    def letter_in_word(word: list, letter: str):
        """Check if the letter is in the word, if it is change the string with underscores
        to show the letter then return a list with the word and the new string.
        """
        new_blank = [c for c in word[1]]
        if any(list(map(lambda x: x[1] == letter, word[0]))):
            for char in list(filter(lambda x: x[1] == letter, word[0])):
                new_blank[char[0]] = char[1]
            word[1] = "".join(new_blank)
            return word
        else:
            tries.append('X')

    def win_condition(chances: int, word: list):
        if "_" not in word[1] and chances < 3:
            print("\nYou won!")
            return True
        else:
            return False

    word = chosen_word(choosing_difficulty())
    count = ["_", "_", "_"]
    while True:
        condition = win_condition(len(tries), word)
        if condition:
            break
        elif len(tries) >= 3:
            count[len(tries) - 1] = tries[len(tries) - 1]
            print(f"\nYou Lose!\nTries: {"".join(count)}\nThe word was: {''.join([w[1] for w in word[0]])}")
            break
        else:
            if tries:
                count[len(tries) - 1] = tries[len(tries) - 1]
            print(f"\nTries: {"".join(count)}\nThe word: {word[1]}")
            letter_in_word(word, verified_input())


if __name__ == "__main__":
    main()
