class Solution:
    def reverse(self, nums, i, j):
        """
        Reverses the elements of the list 'nums' between indices 'i' and 'j' (inclusive).

        Parameters:
        nums (List[int]): The list of integers to be reversed.
        i (int): The starting index of the sublist to be reversed.
        j (int): The ending index of the sublist to be reversed.

        Returns:
        None: The function modifies the list in-place and does not return anything.
        """
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the elements of the given list 'nums' to the right by 'k' steps.

        Parameters:
        nums (List[int]): The list of integers to be rotated.
        k (int): The number of steps to rotate the list.

        Returns:
        None: The function modifies the list in-place and does not return anything.
        """
        n = len(nums)
        k = k % n
        Solution.reverse(self, nums, n - k, n - 1)
        Solution.reverse(self, nums, 0, n - k - 1)
        Solution.reverse(self, nums, 0, n - 1)