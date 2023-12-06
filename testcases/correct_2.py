'''Write a Python function named 'correct_2' that takes two matrices represented as lists of lists (matrix1 and matrix2) as input and returns their matrix product if the multiplication is valid. '''

def correct_2(matrix1, matrix2):
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