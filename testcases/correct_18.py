def correct_18(numRows: int):
    """
    Generate Pascal's Triangle up to the specified number of rows.

    Parameters:
    - numRows (int): The number of rows to generate in Pascal's Triangle.

    Returns:
    List[List[int]]: Pascal's Triangle as a list of lists.
    """
    a = []
    a.append([1])
    for i in range(1, numRows):
        b = []
        for j in range(len(a[i-1])+1):
            if j != 0 and j < len(a[i-1]):
                b.append(a[i-1][j-1]+a[i-1][j])
            else:
                b.append(1)
        a.append(b)
    return a

