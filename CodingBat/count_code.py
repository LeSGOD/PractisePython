# Return the number of times that the string "code" appears anywhere in the given string,
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.


"""
count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2

"""


def count_code(str):
    score = 0
    letters = "abcdefghijklmnopqrstuvwxyz"
    listOfLetters = list(letters)
    x = ["co"+i+"e" for i in listOfLetters]
    for _ in range(2):
        for i in x:
            if i in str:
                score += 1
                index = str.index(i)
                s = list(str)
                for j in range(4):
                    s[index + j] = "1"

                str = "".join(s)

    return score
