'''Write a Python function that calculates the factorial of a non-negative integer 'n' using recursion.'''

def buggy_17(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)