def correct_6(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = correct_6(n-1, memo) + correct_6(n-2, memo)
    return memo[n]
