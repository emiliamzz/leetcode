class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        if len(s) == len(t):
            return s == t
        s_found = 0
        for letter in t:
            if letter == s[s_found]:
                s_found += 1
                if len(s) == s_found:
                    return True
        return False