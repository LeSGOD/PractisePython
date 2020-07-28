"""
Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
i => 2
o => 2
u => 3

# "1lpp0"


Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"

"""

encrypt_dict = {
    "a": 0,
    "e": 1,
    "i": 2,
    "o": 2,
    "u": 3,
}


def encrypt(word):
    encrypted = word[::-1]
    result = ''
    for letter in encrypted:
        if letter in encrypt_dict.keys():
            letter = encrypt_dict[letter]
        result += str(letter)


    return result+str("aca")


print(encrypt('banana'))
