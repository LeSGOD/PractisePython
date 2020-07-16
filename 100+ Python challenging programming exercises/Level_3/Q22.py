"""

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def compute_the_frequency_of_words(sequence):
    sequence = sequence.split(" ")
    sequence_dict = {}
    for key in sequence:
        sequence_dict[key] = 0
    
    for key in sequence_dict.keys():
        for word in sequence:
            if key == word:
                sequence_dict[key] += 1
    
    sorted(sequence_dict)

    for x,y in sequence_dict.items():
        print("{}:{}".format(x,y))



compute_the_frequency_of_words('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')