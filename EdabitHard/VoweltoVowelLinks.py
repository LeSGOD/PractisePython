"""
Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a vowel, 
while the word immediately after begins with a vowel.

Examples
vowel_links("a very large appliance") ➞ True

vowel_links("go to edabit") ➞ True

vowel_links("an open fire") ➞ False

vowel_links("a sudden applause") ➞ False
"""


vowels = ['a', 'e', 'i', 'o', 'u', 'y']


def vowel_links(txt):
    txt = txt.split(" ")
    for i in (0, len(txt)-2):
        if (txt[i][-1] in vowels) and (txt[i+1][0] in vowels):
            return True
    return False
