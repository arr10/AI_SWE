def correct_10(input_list):
    """
    Analyze a list containing both words and numeric strings.

    Parameters:
    - input_list (list): A list containing words and numeric strings.

    Returns:
    dict: A dictionary with the counts of unique words and the sum of numeric values.

    Notes:
    - The function distinguishes between words and numeric strings in the input list.
    - Counts the occurrences of each unique word.
    - Calculates the sum of numeric values in the list.
    - Returns a dictionary with 'word_counts' and 'numeric_sum'.
    """
    word_counts = {}
    numeric_sum = 0

    for item in input_list:
        if isinstance(item, str) and item.isnumeric():
            numeric_sum += int(item)
        elif isinstance(item, str):
            word_counts[item] = word_counts.get(item, 0) + 1

    result_dict = {
        'word_counts': word_counts,
        'numeric_sum': numeric_sum
    }

    return result_dict

def test_correct_10():
    # Test Case 1: Mix of words and numeric strings
    input_list_1 = ['apple', '2', 'banana', '3', 'apple', 'banana', '5']
    result_1 = correct_10(input_list_1)
    expected_result_1 = {'word_counts': {'apple': 2, 'banana': 2}, 'numeric_sum': 10}
    assert result_1 == expected_result_1

    # Test Case 2: Only numeric strings
    input_list_2 = ['1', '2', '3', '4', '5']
    result_2 = correct_10(input_list_2)
    expected_result_2 = {'word_counts': {}, 'numeric_sum': 15}
    assert result_2 == expected_result_2

    # Test Case 3: Only words
    input_list_3 = ['apple', 'banana', 'apple', 'orange', 'banana']
    result_3 = correct_10(input_list_3)
    expected_result_3 = {'word_counts': {'apple': 2, 'banana': 2, 'orange': 1}, 'numeric_sum': 0}
    assert result_3 == expected_result_3

# Run the test cases
test_correct_10()
