def correct_1(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
    - numbers (list): A list of numbers.

    Returns:
    float: The average of the numbers in the input list.
    """
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1

    average = total / count
    return average
