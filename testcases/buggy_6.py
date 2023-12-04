def fibonacci_memoization(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)