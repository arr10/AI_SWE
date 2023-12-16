def weird_input_function(input_list):
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

