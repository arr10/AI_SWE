def fibonacci(n):
    if n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
