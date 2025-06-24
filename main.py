from english_words import get_english_words_set
from random import choice

range_of_words = [
    w
    for w in sorted(list(get_english_words_set(["web2"], lower=True)))
    if len(w) > 3 and len(w) < 7
]

print(choice(range_of_words))
