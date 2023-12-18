def correct_13(x: int) -> bool:
    """
Given an integer x, return true if x is a palindrome, and false otherwise.

Args:
x (int):

Returns:
bool:
"""
    if x<0:
        return False

    inputNum = x
    newNum = 0
    while x>0:
        newNum = newNum * 10 + x%10
        x = x//10
    return newNum == inputNum


def test_correct_13():
    assert correct_13(121) == True
    assert correct_13(10) == False
    assert correct_13(-121) == False

test_correct_13()