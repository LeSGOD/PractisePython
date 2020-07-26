"""Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. 
if Bob is not in the array, return -1.
"""


def find_bob(names):
    
    if "Bob" in names:
        return names.index("Bob")
        
    else:
        return -1 

#find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2