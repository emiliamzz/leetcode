class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        count = 0
        longest = 0
        i = 0
        while len(s) > 0:
            if i == len(s):
                if count > longest:
                    longest = count
                break
            if s[i] in s[:i]:
                if count > longest:
                    longest = count
                count = 0
                s = s[s.index(s[i])+1:]
                i = 0
            else:
                i += 1
                count += 1
        return longest