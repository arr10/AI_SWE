def correct_7(input_string):
    result = ""

    for char in input_string:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char

    return result