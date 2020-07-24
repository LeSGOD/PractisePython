"""
Write the regular expression that will match all non-digit characters of a string. Use the character class \D in your expression.
"""
import re

txt = "242Edabit2345can3443be3254324addictive"

pattern = "\D+"

result = " ".join(re.findall(pattern, txt))
