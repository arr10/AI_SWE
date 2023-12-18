def correct_17(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    - n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the input integer.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * correct_17(n - 1)