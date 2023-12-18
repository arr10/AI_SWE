import numpy as np

def correct_4(input_array):
    """
    Multiply each element in a NumPy array by 2.

    Parameters:
    - input_array (numpy.ndarray): The input NumPy array.

    Returns:
    numpy.ndarray: A new array with each element multiplied by 2.
    """
    rows, cols = input_array.shape
    result = np.zeros_like(input_array)

    for i in range(rows):
        for j in range(cols):
            result[i, j] = input_array[i, j] * 2

    return result