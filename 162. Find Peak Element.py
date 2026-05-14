class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            i = int((right - left) / 2) + left
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            if nums[i-1] >= nums[i+1]:
                right = i - 1
            else:
                left = i + 1
        if nums[left] >= nums[right]:
            return left
        return right