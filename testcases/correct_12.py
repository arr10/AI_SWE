def correct_12(nums) -> int:
    """
    The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d)
    Args:
        Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

    Returns:
        Return the maximum such product difference.
    """
    min1 = min2 = float('inf')
    max1 = max2 = float('-inf')
    for n in nums:
        if n <= min1:
            min1, min2, = n, min1
        elif n < min2:
            min2 = n
        if n >= max1:
            max1, max2 = n, max1
        elif n > max2:
            max2 = n
    return max1*max2-min1*min2

