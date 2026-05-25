class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        low = 0
        high = len(citations) - 1
        h = 0
        while high - low > 1:
            mid = round((high - low) / 2) + low
            if citations[mid] > mid:
                if mid + 1 > h:
                    h = mid + 1
                low = mid
            else:
                high = mid
        if high - low == 1:
            if citations[high] > high:
                if high + 1 > h:
                    h = high + 1
            elif citations[low] > low:
                if low + 1 > h:
                    h = low + 1
        elif low == high:
            if citations[low] > low:
                if low + 1 > h:
                    h = low + 1
        return h