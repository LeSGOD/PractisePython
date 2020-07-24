"""
The caret ^, when found at the start of a characer set, is the equivalent to "not" in RegEx. 
The regular expression [^a-c] matches any characters except "a", "b" and "c". 
Write the regular expression that matches any characters except letters, digits and spaces. You must use a negated character set in your expression.
"""


import re

txt = " alice15@gmail.com "
pattern = "[^\w\s]"

re.findall(pattern, txt) #["@", "."]
