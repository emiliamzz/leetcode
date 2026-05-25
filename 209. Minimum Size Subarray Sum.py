class Solution:
    def window(self, target: int, nums: List[int], size: int) -> bool:
        total = sum(nums[:size])
        if total >= target:
            return True
        i = 0
        while i + size < len(nums):
            total -= nums[i]
            total += nums[i+size]
            if total >= target:
                return True
            i += 1
        return False

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 1
        high = len(nums)
        smallest = None
        while high - low > 1:
            mid = round((high - low) / 2) + low
            does_window = self.window(target, nums, mid)
            if not does_window:
                low = mid + 1
            else:
                if smallest == None or mid < smallest:
                    smallest = mid
                high = mid - 1
        if smallest == None or low < smallest:
            if self.window(target, nums, low):
                return low
        if smallest == None or high < smallest:
            if self.window(target, nums, high):
                return high
        if smallest != None:
            return smallest
        return 0