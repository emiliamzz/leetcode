class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        volume = min(height[a], height[b]) * (b - a)
        while a != b - 1:
            if height[a] <= height[b]:
                a += 1
            else:
                b -= 1
            new = min(height[a], height[b]) * (b - a)
            if new > volume:
                volume = new
        return volume