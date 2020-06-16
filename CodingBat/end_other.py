"""
Given two strings, return True if either of the strings appears at the very end of the other string,
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""

# One way to solve the problem


def end_other1(a, b):
    a = a.upper()
    b = b.upper()
    if a in b or b in a:
        if a[-1] == b[-1] or b[-1] == a[-1]:
            return True
    return False

# Second way to solve the problem


def end_other2(a, b):
    a = a.lower()
    b = b.lower()
    return (b.endswith(a) or a.endswith(b))
