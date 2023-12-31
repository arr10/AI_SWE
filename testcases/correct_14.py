def correct_14(a: str, b: str) -> str:
    """
    Given two binary strings a and b, return their sum as a binary string.
    
    Args:
        a (str): first binary string
        b (str): second binary string

    Returns:
        str: their binary sum
    """
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        s.append(str(carry % 2))
        carry //= 2

    return ''.join(reversed(s))


def test_correct_14():
    assert correct_14("11", "1") == "100"
    assert correct_14("1010", "1011") == "10101"
    
test_correct_14()