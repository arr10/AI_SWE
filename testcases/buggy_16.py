'''Write a Python function that calculates the nth Fibonacci number using recursion. The function should be named 'buggy_16' and take an integer parameter 'n'.'''

def buggy_16(n):
    if n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
