"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sub"
SUPERLIST = "super"
EQUAL = "=="
UNEQUAL = "!="

def sliding_window(shorter, longer) -> bool:
    for i in range(len(longer) - len(shorter) + 1):
        if longer[i:i + len(shorter)] == shorter:
            return True    
    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if len(list_one) > len(list_two) and sliding_window(list_two, list_one):
        return SUPERLIST
    if len(list_one) < len(list_two) and sliding_window(list_one, list_two):
        return SUBLIST    
    return UNEQUAL