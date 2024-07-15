from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
    """
    Remove duplicates from a sorted list of integers and return the new length of the list.

    The function uses a set to keep track of unique elements in the input list.
    It then iterates over the sorted set and updates the original list with unique elements.
    The function returns the new length of the list after removing duplicates.

    Parameters:
    nums (List[int]): The input list of integers, which is assumed to be sorted in ascending order.

    Returns:
    int: The new length of the list after removing duplicates.
    """
    se = set()
    for i in nums:
        se.add(i)

    index = 0
    for i in sorted(se):
        nums[index] = i
        index += 1
    return index