class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        low = 1
        high = len(strs[0])
        ans = low
        if high == 0:
            return ""
        prefix = strs[0][0]
        for word in strs:
            if len(word) == 0:
                return ""
            if word[0] != prefix:
                return ""
            if len(word) < high:
                high = len(word)
        while low <= high:
            mid = int((high - low) / 2) + low
            prefix = strs[0][:mid]
            all_match = True
            for word in strs:
                if word[:mid] != prefix:
                    high = mid - 1
                    all_match = False
                    break
            if all_match:
                ans = mid
                low = mid + 1
        return strs[0][:ans]