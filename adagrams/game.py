from random import randint
import collections 

# global pool of letters
POOL = {
    "A": 9, "B": 2, "C": 2, "D": 4, 
    "E": 12,  "F": 2,  "G": 3,  "H": 2, 
    "I": 9 , "J": 1,  "K":1,  "L": 4, 
    "M": 2, "N": 6, "O": 8 , "P": 2, "Q": 1,
    "R":6, "S" : 4, "T": 6, "U":4, "V": 2, "W":2 
    , "X": 1, "Y":2, "Z": 1 
}

SCORE_WORD = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F" ,"H", "V", "W", "Y"],
    5:["K"],
    8:["J", "X"],
    10:["Q", "Z"]
}

def draw_letters():
    letter_pool = convert_dict_to_list(POOL)
    random_array = []

    for _ in range(10):
        random_index = randint(0, len(letter_pool) - 1)
        random_letter = letter_pool.pop(random_index)
        random_array.append(random_letter)

    return random_array
# =============== helper functions =============
def convert_dict_to_list(dict):
    letters = []
    for letter, quantity in POOL.items():
        for _ in range(quantity):
            letters.append(letter)
    return letters

# ========================================================

def uses_available_letters(word, letter_bank):
    """
        word: string input word
        letter_bank: array of drawn letters in a hand.
    """
    is_available = True
    word_dict = collections.Counter(word.upper())
    letter_bank_dict = collections.Counter(letter_bank)

    for letter, count in word_dict.items():
        if letter_bank_dict[letter] >= count:
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
    _word = word.upper()

    for letter in _word:
        for key,letters in SCORE_WORD.items():
            if letter in letters:
                score+= key

    if len(word)>= 7 and len(word)<= 10:
        score+= 8

    return score


def get_highest_word_score(word_list):
    pass