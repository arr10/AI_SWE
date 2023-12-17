def correct_3(value, my_list=None):
    """
    Add a value to a list. If the list is not provided, create a new one.

    Parameters:
    - value: The value to add to the list.
    - my_list (list, optional): The list to which the value should be added. If not provided, a new list is created.

    Returns:
    list: The updated list after adding the value.
    """
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

