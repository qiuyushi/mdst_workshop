"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    return x % 2 == 0

def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    for i in range(1, len(word)):
        if word[i] != word[-1 * i]:
            return False
    return True


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    count = 0
    list = []
    for num in numlist:
        if is_odd(num):
            list[count] = num
            count += 1
    return list



def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    str_list = []
    lines = text.split("\n")
    for line in lines:
        str_list += line.split
    return str_list

