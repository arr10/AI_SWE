def correct_11(input):
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

def test_correct_11():
    # Test Case 1: General case
    input_1 = [1, 3, 5, 2, 6, 4]
    
    # Test Case 2: Edge case with all elements identical
    input_2 = [3, 3, 3, 3, 3]
    
    # Test Case 3: Small input list
    input_3 = [2, 4, 3]
    
    # Run tests
    assert correct_11(input_1) == [2, 4]
    assert correct_11(input_2) == []
    assert correct_11(input_3) == [1]

test_correct_11()