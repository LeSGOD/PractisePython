"""
Write a regular expression that will help us count how many tall people work in your company. You must use RegEx positive lookbehind.
"""
import re

lst = ["tall height", "tall height", "short height", "medium height", "tall height"]
pattern = "(?<=tall)"

len(re.findall(pattern, ", ".join(lst))) #3
