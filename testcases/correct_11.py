def find_peaks(input):
    """
    Finds indices where the element is greater than its adjacent elements in the input list.

    Args:
    - input: List of elements

    Returns:
    - List containing indices where the element is greater than both its preceding and succeeding elements.
    """
    res = []
    for i in range(1, len(input) - 1):
        if input[i] > input[i - 1] and input[i] > input[i + 1]:
            res.append(i)
    return res