"""
Exercise - Tribonacci 🔢
Now that we’ve learned about the power of memoization through the Fibonacci sequence, 
let’s explore another sequence that benefits from memoization: the Tribonacci sequence.

The Tribonacci sequence is an expansion of the Fibonacci sequence where each term is 
the sum of the three preceding terms, rather than two. 
The sequence starts as: 0, 0, 1, 1, 2, 4, 7, 13, 24, 44,…

Tribonacci: Write a Python program to calculate the n-th number in the Tribonacci sequence 
using memoization (where tribonacci(0) returns the first element of the sequence, 0).
Your recursive solution should use memoization, i.e. utilize a dictionary or a list to 
store previously computed results to ensure optimal computation.

"""

def tribo_memo(n):
    memo = {}
    return tribonacci(n, memo)

def tribonacci(n, memo):
    print(f"tribonacci({n}, {memo})")
    if n in memo:
        return memo[n]
    if n <= 2:
        return n
    result = tribonacci(n-1, memo) + tribonacci(n-2, memo) + tribonacci(n-3, memo)
    memo[n] = result
    return result

print("The 10th number in the Tribonacci sequence is: " + str(tribo_memo(10)))
print("The 9th number in the Tribonacci sequence is: " + str(tribo_memo(9)))

