class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ranges = [str(nums[0])]
        last = nums[0]
        if len(nums) == 1:
            return ranges
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if nums[i-1] != last:
                    ranges[-1] += '->' + str(nums[i-1])
                ranges.append(str(nums[i]))
                last = nums[i]
        if last != nums[-1]:
            ranges[-1] += '->' + str(nums[-1])
        return ranges