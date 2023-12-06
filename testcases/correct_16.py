'''Write a Python function that calculates the nth Fibonacci number using recursion. The function should be named 'correct_16' and take an integer parameter 'n'.'''

def correct_16(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)