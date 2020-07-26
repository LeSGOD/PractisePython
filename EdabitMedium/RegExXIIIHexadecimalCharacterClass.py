"""
You might get text that looks like it's all English characters but it very well may not be: pànts != pants

To ensure that you only get the characters you want in a string you will need to use the character classes that accept hexadecimal digits.

Write a regular expression that will match the word "edabit". Use the hexadecimal character classes \x or \u in your expression.

You are not allowed to use any of the following characters: \w, \W, \d, \D, \t, \T, \S, \c, ., [, ] as well as any of the letters in the word edabit.
"""

import re

txt = "edabit"
pattern = u'65 64 61 62 69 74 0a '

bool(re.match("^{}$".format(pattern), txt))
