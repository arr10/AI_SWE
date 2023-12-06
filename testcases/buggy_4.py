'''Write a Python function named 'buggy_4' that takes a NumPy array ('input_array') as input and returns a new array where each element is multiplied by 2.'''

import numpy as np

def bugg_4(input_array):
    rows, cols = input_array.shape
    result = np.zeros_like(input_array)

    for i in range(rows):
        for j in range(cols):
            result[i, j] = input_array[i, j] * 2

    return result
