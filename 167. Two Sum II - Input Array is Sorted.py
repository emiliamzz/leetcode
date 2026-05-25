class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1, 2]
        for i in range(len(numbers)):
            remainder = target - numbers[i]
            if remainder in numbers:
                j = numbers.index(remainder)
                if j == i:
                    j += 1
                return [i+1, j+1]