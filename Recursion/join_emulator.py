"""
Join List with Separator: Write a recursive function join_recursive(lst, sep) that emulates
Python’s str.join() method. This function should join a list of strings with a given separator.
For instance, join_recursive(['a', 'b', 'c'], '-') should return 'a-b-c'.
"""

def join_recursive(lst, sep):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sep + join_recursive(lst[1:], sep)

print(f"Joining ['a', 'b', 'c'] with '-':")
print(join_recursive(['a', 'b', 'c'], '-'))

