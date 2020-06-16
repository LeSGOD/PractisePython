"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

"""

def string_splosion(str):
    s = list(str)
    word = ""
    for i in range(len(s)+1):
        w = "".join(s[:i])
        word += w
    return word




