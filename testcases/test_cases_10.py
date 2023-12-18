def test_cases_10():
    # Test Case 1: Mix of words and numeric strings
    input_list_1 = ['apple', '2', 'banana', '3', 'apple', 'banana', '5']
    result_1 = buggy_10(input_list_1)
    expected_result_1 = {'word_counts': {'apple': 2, 'banana': 2}, 'numeric_sum': 10}
    assert result_1 == expected_result_1

    # Test Case 2: Only numeric strings
    input_list_2 = ['1', '2', '3', '4', '5']
    result_2 = buggy_10(input_list_2)
    expected_result_2 = {'word_counts': {}, 'numeric_sum': 15}
    assert result_2 == expected_result_2

    # Test Case 3: Only words
    input_list_3 = ['apple', 'banana', 'apple', 'orange', 'banana']
    result_3 = buggy_10(input_list_3)
    expected_result_3 = {'word_counts': {'apple': 2, 'banana': 2, 'orange': 1}, 'numeric_sum': 0}
    assert result_3 == expected_result_3

# Run the test cases
test_cases_10()
