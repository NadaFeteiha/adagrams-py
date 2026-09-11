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


def get_letter_frequency(word):
    frequency = {}
    for letter in word:
        letter = letter.upper()
        frequency[letter] = frequency.get(letter, 0) + 1
    return frequency
# ========================================================
