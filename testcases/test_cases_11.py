def test_cases_11():
    # Test Case 1: General case
    input_1 = [1, 3, 5, 2, 6, 4]
    
    # Test Case 2: Edge case with all elements identical
    input_2 = [3, 3, 3, 3, 3]
    
    # Test Case 3: Small input list
    input_3 = [2, 4, 3]
    
    # Run tests
    assert buggy_11(input_1) == [2, 4]
    assert buggy_11(input_2) == []
    assert buggy_11(input_3) == [1]

test_cases_11()
