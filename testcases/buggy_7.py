def buggy_7(input_string):
    '''
    This function reverses the case of the alphabetic characters in the input string.
    If the alphabetic char is lower case, it makes it upper case and vice verse. 
    It leaves the numeric and other characters as it is
    '''
    
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
