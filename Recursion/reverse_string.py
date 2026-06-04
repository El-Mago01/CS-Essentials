"""
Reverse a String:
Write a recursive function reverse_string(s) to reverse a given string s.
For instance, reverse_string(‘hello’) should return ‘olleh’.
"""
def reverse_string(s):
    if len(s) == 1:
        return s
    return s[-1] + reverse_string(s[:-1])

print(f"Original string: 'hello'")
print("Reversed string: " + str(reverse_string('hello')))

