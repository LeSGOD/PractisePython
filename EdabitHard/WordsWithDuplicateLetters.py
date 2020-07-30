"""
Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.

Examples
no_duplicate_letters("Fortune favours the bold.") ➞ True

no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True

no_duplicate_letters("Look before you leap.") ➞ False
# Duplicate letters in "Look" and "before".

no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
# Duplicate letters in "apple", "keeps", "doctor", and "away".
"""
import string


def no_duplicate_letters(phrase):
    phrase_lst = phrase.split(" ")
    for word in phrase_lst:

        word_dict = {}
        word_lst = " ".join(word).split(" ")

        for letter in word_lst:
            try:
                word_dict[letter] += 1
            except KeyError:
                word_dict[letter] = 1

        if max(word_dict.values()) >= 2:
            return False

    return True
