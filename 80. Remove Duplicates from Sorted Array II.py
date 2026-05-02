class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        count = 1
        num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == num:
                count += 1
                if count > 2:
                    nums[i] = '_'
            else:
                num = nums[i]
                count = 1
        for i in range(len(nums)-1):
            if nums[i] == '_':
                for j in range(i+1, len(nums)):
                    if nums[j] != '_':
                        nums[i] = nums[j]
                        nums[j] = '_'
                        break
                    if j == len(nums) - 1:
                        return(len(nums) - nums.count('_'))
        return(len(nums) - nums.count('_'))