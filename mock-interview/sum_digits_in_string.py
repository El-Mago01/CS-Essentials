"""
Sum of Digits in a String
Description:

Create a function sum_of_digits(text) that returns the sum of all digits found in the given string. Non-digit characters should be ignored.

Test Data:

input_text = "abc123xyz45"

# Expected digits: 1, 2, 3, 4, 5 => total = 15

print(sum_of_digits(input_text))  # Output: 15
"""

# Check difference between set and list
# check use case tuple packing unpacking
# could have added the swap mechanism
# 15 minutes per exercise.
# Excellent score.
# AI track would more specialized track. AI powered application and agents.
# Profile is aligned



def sum_of_digits(text):
    total = 0
    for char in text:
        if char.isdigit():
            total += int(char)
    return total


def main():
    input_text = "abc123xyz45"
    print(sum_of_digits(input_text))

if __name__ == "__main__":
    main()