class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        arr = [None] * len(nums)
        arr[0] = 0
        for i in range(len(nums)):
            for j in range(nums[i], 0, -1):
                if i + j > len(nums) - 1:
                    continue
                if i + j == len(nums) - 1:
                    return arr[i] + 1
                if arr[i+j] == None:
                    arr[i+j] = arr[i] + 1