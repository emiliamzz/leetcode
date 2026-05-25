class Solution:

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        nums.reverse()
        final_jump = False
        if nums[0] == 0:
            final_jump = True
        while 0 in nums:
            nums = nums[nums.index(0):]
            count = 0
            for num in nums:
                if num == 0:
                    count += 1
                else:
                    break
            nums = nums[count:]
            found = False
            for i in range(len(nums)):
                if final_jump:
                    if nums[i] >= i + count:
                        found = True
                        final_jump = False
                        break
                elif nums[i] > i + count:
                    found = True
                    break
            if not found:
                return False
        return True