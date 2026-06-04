"""
The Fibonacci sequence is a well-known mathematical sequence
where each number is the sum of the two preceding ones.
The sequence starts like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …

Given a number n, our task is to compute the n’th Fibonacci number.
Although this task can be solved in an iterative manner,
we will explore the recursive approach to better understand its
characteristics and improvements.
"""

def fib(n):
    # Stopping condition: fib(0) = 0, fib(1) = 1
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(30))

"""
Improving with Memoization 🚀
To optimize our solution, we can use an approach known as memoization. 
This is a technique used in computer programming to optimize programs by storing 
the results of expensive function calls and reusing them when the same inputs occur again.

To apply memoization in our Fibonacci calculation, we use an envelope function, fib_memo(), 
that initiates the memo dictionary and calls the helper function, _fib_memo_helper(). 
The helper function then performs the actual recursive calculation and memoization.
"""

def fib_memo(n):
    memo = {}  # Initialize an empty memo dictionary
    return _fib_memo_helper(n, memo)

def _fib_memo_helper(n, memo):
    if n in memo:  # If result is in memo, return it
        return memo[n]
    elif n <= 1:  # Base case: return n
        return n
    else:
        # If not in memo, calculate it recursively and add it to memo
        result = _fib_memo_helper(n-1, memo) + _fib_memo_helper(n-2, memo)
        memo[n] = result
        return result

print(fib_memo(5))


