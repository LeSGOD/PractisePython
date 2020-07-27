"""
Create a function that takes a string and returns the number (count) of vowels contained within it.
"""

def count_vowels(txt):
	vowels = ['a', 'e', 'i', 'o', 'u']
	result = 0
	for item in txt:
			if item in vowels:
					result += 1
	return result 