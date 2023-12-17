import numpy as np

def buggy_4(input_array):
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
        result[i] = input_array[i] * 2

    return result
