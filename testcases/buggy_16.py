def buggy_16(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Parameters:
    - n (int): The index of the Fibonacci number to calculate.

    Returns:
    int: The nth Fibonacci number.

    Notes:
    - The function uses recursion to calculate the Fibonacci number for the given index.
    - If n is 0, the function returns 0.
    - If n is 1, the function returns 1.
    - For n greater than 1, the function recursively calculates the Fibonacci number for n-1 and n-2,
      sums them, and returns the result.
    """
    if n == 0:
        return 0
    else:
        return buggy_16(n - 1) + buggy_16(n - 2)
