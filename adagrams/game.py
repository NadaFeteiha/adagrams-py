from random import randint
# global pool of letters
pool = {
    "A": 9, "B": 2, "C": 2, "D": 4, 
    "E": 12,  "F": 2,  "G": 3,  "H": 2, 
    "I": 9 , "J": 1,  "K":1,  "L": 4, 
    "M": 2, "N": 6, "O": 8 , "P": 2, "Q": 1,
    "R":6, "S" : 4, "T": 6, "U":4, "V": 2, "W":2 
    , "X": 1, "Y":2, "Z": 1 
}

def draw_letters():
    letter_pool = convert_dict_to_list(pool)
    random_array = []

    for _ in range(10):
        random_index = randint(0, len(letter_pool) - 1)
        random_letter = letter_pool.pop(random_index)
        random_array.append(random_letter)

    return random_array
# =============== helper functions =============
def convert_dict_to_list(dict):
    letters = []
    for letter, quantity in pool.items():
        for _ in range(quantity):
            letters.append(letter)
    return letters

# ========================================================

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass