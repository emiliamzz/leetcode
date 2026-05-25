class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            elif nums[0] <= target:
                return 1
            else:
                return 0
        min_index = 0
        max_index = len(nums) - 1
        middle_index = len(nums) // 2
        while True:
            if min_index == max_index:
                if target == nums[min_index]:
                    return min_index
                if target < nums[min_index]:
                    return min_index
                return min_index + 1
            if (max_index - min_index) == 1:
                if nums[min_index] == target:
                    return min_index
                if nums[max_index] == target:
                    return max_index
                if target < nums[min_index]:
                    return min_index
                if target < nums[max_index]:
                    return max_index
                return max_index + 1
            if nums[middle_index] == target:
                return middle_index
            if target < nums[middle_index]:
                max_index = middle_index - 1
            else:
                min_index = middle_index + 1
            middle_index = (max_index - min_index) // 2 + min_index