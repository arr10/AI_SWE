def correct_15(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


    Args:
        nums ([int]): integer list

    Returns:
        Boolean value: True if there is duplicate, else false
    """
    hset = set()

    for n in nums:
        if n in hset:
            return True
        else:
            hset.add(n)
    
    return False
