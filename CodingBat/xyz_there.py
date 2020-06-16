"""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.).
 So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

"""

def xyz_there(str):
    if ".xyz" in str:
        word = str.replace(".xyz", "1")
        if "xyz" in word:
            return True
        return False
    if "xyz" in str:
        return True
    return False