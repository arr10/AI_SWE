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

def test_correct_15():
    assert correct_15([1,2,3,1]) == True
    assert correct_15([1,2,3,4]) == False
    assert correct_15([1,1,1,3,3,4,3,2,4,2]) == True

test_correct_15()