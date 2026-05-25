class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]
        i = -1
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
            if (i * -1) > len(digits):
                digits.insert(0, 1)
                return digits
        digits[i] += 1
        return digits