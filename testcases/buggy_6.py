def buggy_6(n, memo={}):
    '''
    This is a recursive function that implements the fibonacci sequence
    '''
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = buggy_6(n-1, memo) + buggy_6(n-2, memo)