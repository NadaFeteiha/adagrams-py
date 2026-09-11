from random import randint
from .logic_helper import *
from .constants import *


def draw_letters():
    letter_pool = convert_dict_to_list(POOL)
    random_array = []

    for _ in range(10):
        random_index = randint(0, len(letter_pool) - 1)
        random_letter = letter_pool.pop(random_index)
        random_array.append(random_letter)

    return random_array

def uses_available_letters(word, letter_bank):
    """
    word: string input word
    letter_bank: array of drawn letters in a hand.
    """
    word_dict = get_letter_frequency(word)
    letter_bank_dict = get_letter_frequency(letter_bank)

    for letter, count in word_dict.items():
        if letter_bank_dict.get(letter, 0) >= count:
            continue
        else:
            return False

    return True


def score_word(word):
    """
    word: string of characters
    Returns  integer representing the number of points
    """
    score = 0

    for letter in word:
        score += LETTER_SCORE[letter.upper()]

    if len(word) >= 7 and len(word) <= 10:
        score += 8

    return score


def get_highest_word_score(word_list):
    """
    word_list: list of submitted words

    main condition to win:
        - the highest score

    in case of a tie (same highest score):
        - the word with the fewest letters wins
        - unless one of the tied words has exactly 10 letters,
          then that 10-letter word wins instead
        - if still tied (same score, same length), the first
          word in word_list wins
    """
    if not word_list:
        return ("", 0)

    # group words by their score, so words sharing the top score are kept together
    words_score = {}
    for word in word_list:
        score = score_word(word)
        if score not in words_score:
            words_score[score] = []
        words_score[score].append(word)

    all_scores = list(words_score.keys())
    max_score = find_max(all_scores)

    tied_words = words_score[max_score]

    # tie-break rule 1: a 10-letter word beats any other length
    ten_letter_word = None
    for word in tied_words:
        if len(word) == 10:
            ten_letter_word = word
            break

    if ten_letter_word:
        winning_word = ten_letter_word
    else:
        # tie-break rule 2: otherwise the shortest word wins;
        # using "<" (not "<=") keeps the first word seen on equal length,
        # which covers tie-break rule 3 (same score and length -> first in list)
        winning_word = tied_words[0]
        for word in tied_words:
            if len(word) < len(winning_word):
                winning_word = word

    return (winning_word, max_score)
