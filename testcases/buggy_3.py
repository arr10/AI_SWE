'''Write a Python function named 'buggy_3' that takes a value and an optional list ('my_list') as parameters. If 'my_list' is not provided, initialize an empty list. Append the given value to 'my_list' and return the modified list.'''

def buggy_3(value, my_list=[]):
    my_list.append(value)
    return my_list
