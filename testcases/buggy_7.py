def buggy_7(input_string):
    """
    Swap the case of alphabetic characters in a given string while leaving non-alphabetic characters unchanged.

    Parameters:
    - input_string (str): The input string to perform case swapping on.

    Returns:
    str: A new string with the case of alphabetic characters swapped and non-alphabetic characters unchanged.

    Notes:
    - The function iterates through each character in the input string.
    - If a character is alphabetic and in lowercase, it is converted to uppercase.
    - If a character is alphabetic and in uppercase, it is converted to lowercase.
    - Non-alphabetic characters are unchanged.
    - The result is a new string with the desired case-swapping applied.
    """
    result = ""

    for char in input_string:
        if char.isalpha():
            if char.islower():
                result = char.upper()
            else:
                result += char.lower()
        else:
            result += char

    return result
