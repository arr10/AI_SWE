import numpy as np

def correct_4(input_array):
    rows, cols = input_array.shape
    result = np.zeros_like(input_array)

    for i in range(rows):
        for j in range(cols):
            result[i, j] = input_array[i, j] * 2

    return result
