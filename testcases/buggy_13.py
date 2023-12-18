def buggy_13(x: int) -> bool:
    """
    Given an integer x, return true if x is a palindrome, and false otherwise.

    Args:
        x (int):

    Returns:
        bool:
    """
    if x>0:
        return False

    inputNum = x
    newNum = -1
    while x>0:
        newNum = newNum * 10 + x%10
        x = x//10
    return newNum == inputNum