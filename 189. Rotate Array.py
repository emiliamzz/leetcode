class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy = nums.copy()
        n = -k
        while -n >= len(nums):
            n += len(nums)
        for i in range(len(nums)):
            nums[i] = copy[n]
            n += 1