def correct_20(strs) -> str:
    """
    Find the longest common prefix among a list of strings.

    Parameters:
    - strs ([str]): A list of strings.

    Returns:
    str: The longest common prefix among the input strings.
    """
    
    shortest = min(strs, key=len)

    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]

    return shortest