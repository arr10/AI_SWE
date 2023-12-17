import numpy as np

def test_cases_4():
    array = np.array([[1, 2, 3], [4, 5, 6]])
    assert buggy_4(array) == np.array([[2, 4, 6], [8, 10, 12]])
    
    array = np.array([[1, 3, 7, 8, 10, 5], 
                     [0, 5, 2, 10, 1, 6]])
    assert buggy_4(array) == np.array([[ 2,  6, 14, 16, 20, 10],
                                       [ 0, 10,  4, 20,  2, 12]])
    
    array = np.array([[0, 3], [2, 4], [5, 10], [4, 4], [1, 1], 
                     [4, 2], [1, 8], [3, 7], [9, 7], [9, 1]])
    assert buggy_4(array) == np.array([[ 0,  6], [ 4,  8], [10, 20], [ 8,  8], [ 2,  2], 
                                        [ 8,  4], [ 2, 16], [ 6, 14], [18, 14], [18,  2]])

test_cases_4()
    
    