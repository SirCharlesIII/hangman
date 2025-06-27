from random import choice
from english_words import get_english_words_set
from re import findall


def main():
    tries = 1
    tried_letter = []
    words = list(get_english_words_set(["web2"], lower=True))

    def chosen_word(difficulty: list):
        word = choice(difficulty)
        return [word, "_" * len(word)]

    def choosing_difficulty():
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
        indexes = list(enumerate(word[0]))
        new_blank = [w for w in word[1]]
        for char in list(filter(lambda x: x[1] == letter, indexes)):
            new_blank[char[0]] = char[1]
        word[1] = "".join(new_blank)
        return word

    word = chosen_word(choosing_difficulty())
    checked_letter = letter_in_word(word, verified_input())

    print(checked_letter)


if __name__ == "__main__":
    main()
