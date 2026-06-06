class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        nums = list(set(nums))
        nums.sort()
        max_count = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1
        if count > max_count:
            return count
        return max_count