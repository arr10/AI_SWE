'''Write a Python function named 'correct_3' that takes a value and an optional list ('my_list') as parameters. If 'my_list' is not provided, initialize an empty list. Append the given value to 'my_list' and return the modified list. Append the given value to 'my_list' and return the modified list.'''

def correct_3(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list
