def buggy_6(n, memo={}):
    """
    Calculate the nth Fibonacci number using memoization.

    Parameters:
    - n (int): The index of the Fibonacci number to calculate.
    - memo (dict): A dictionary to store previously calculated Fibonacci numbers for memoization.

    Returns:
    int: The nth Fibonacci number.

    Notes:
    - The function uses memoization to optimize the calculation by storing previously
      computed Fibonacci numbers in the 'memo' dictionary.
    - If n is 0 or 1, the function returns n directly.
    - If n is greater than 1 and not already in the memo dictionary, the function recursively
      calculates the Fibonacci number for n-1 and n-2, sums them, and stores the result in memo[n].
    - The final result is memo[n], representing the nth Fibonacci number.
    """
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = buggy_6(n-1, memo) + buggy_6(n-2, memo)