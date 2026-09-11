from random import randint

# global pool of letters
POOL = {
    "A": 9,
    "B": 2,
    "C": 2,
    "D": 4,
    "E": 12,
    "F": 2,
    "G": 3,
    "H": 2,
    "I": 9,
    "J": 1,
    "K": 1,
    "L": 4,
    "M": 2,
    "N": 6,
    "O": 8,
    "P": 2,
    "Q": 1,
    "R": 6,
    "S": 4,
    "T": 6,
    "U": 4,
    "V": 2,
    "W": 2,
    "X": 1,
    "Y": 2,
    "Z": 1,
}

SCORE_WORD = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"],
}

LETTER_SCORE = {}
for _score, _letters in SCORE_WORD.items():
    for _letter in _letters:
        LETTER_SCORE[_letter] = _score


def draw_letters():
    letter_pool = convert_dict_to_list(POOL)
    random_array = []

    for _ in range(10):
        random_index = randint(0, len(letter_pool) - 1)
        random_letter = letter_pool.pop(random_index)
        random_array.append(random_letter)

    return random_array


# =============== helper functions =============
def convert_dict_to_list(letter_pool_dict):
    letters = []
    for letter, quantity in letter_pool_dict.items():
        for _ in range(quantity):
            letters.append(letter)
    return letters

def find_max(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def get_capitalize_letter_frequently(word):
    output ={}
    for c in word:
        c = c.upper()
        output[c] = output.get(c, 0) + 1
    return output

# ========================================================


def uses_available_letters(word, letter_bank):
    """
    word: string input word
    letter_bank: array of drawn letters in a hand.
    """
    is_available = True
    word_dict = get_capitalize_letter_frequently(word)
    letter_bank_dict = get_capitalize_letter_frequently(letter_bank)

    for letter, count in word_dict.items():
        if letter_bank_dict.get(letter, 0) >= count:
            continue
        else:
            return False

    return is_available


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
    if not word_list:
        return ("", 0)

    words_score = {}

    for word in word_list:
        score = score_word(word)
        if score not in words_score:
            words_score[score] = []
        words_score[score].append(word)

    all_scores = list(words_score.keys())
    max_score = find_max(all_scores)

    tied_words = words_score[max_score]

    ten_letter_word = None
    for word in tied_words:
        if len(word) == 10:
            ten_letter_word = word
            break

    if ten_letter_word:
        winning_word = ten_letter_word
    else:
        winning_word = tied_words[0]
        for word in tied_words:
            if len(word) < len(winning_word):
                winning_word = word

    return (winning_word, max_score)
