def buggy_17(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    - n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the input integer.
    """
    if n == 0:
        return 1
    else:
        return n * buggy_17(n - 1)