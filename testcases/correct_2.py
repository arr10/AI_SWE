def correct_2(matrix1, matrix2):
    """
    Multiply two matrices.

    Parameters:
    - matrix1 (list of lists): The first matrix.
    - matrix2 (list of lists): The second matrix.

    Returns:
    list of lists: The result of multiplying the two matrices.
    If the matrices are not compatible for multiplication, returns 0.
    """
    try:
        assert len(matrix1[0]) == len(matrix2)
    except AssertionError:
        return 0
    
    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    
    return result
