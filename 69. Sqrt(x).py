class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        min = 1
        max = x // 2
        while True:
            if min == max:
                return min
            if (max - min) == 1:
                if (max * max) <= x:
                    return max
                return min
            middle = (max - min) // 2 + min
            sqrt = middle * middle
            if sqrt == x:
                return middle
            if sqrt < x:
                min = middle
            else:
                max = middle
