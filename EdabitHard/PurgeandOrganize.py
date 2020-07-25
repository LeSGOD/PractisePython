"""
Given a list of numbers, write a function that returns a list that...

Has all duplicate elements removed.
Is sorted from least to greatest value.
"""

def unique_sort(lst):
	return sorted(list(dict.fromkeys(lst)))



