class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a = s.split(' ')
        if len(pattern) != len(a):
            return False
        mapping_pattern = {}
        mapping_a = {}
        for i in range(len(a)):
            if pattern[i] in mapping_pattern:
                if mapping_pattern[pattern[i]] != a[i]:
                    return False
            else:
                mapping_pattern[pattern[i]] = a[i]
            if a[i] in mapping_a:
                if mapping_a[a[i]] != pattern[i]:
                    return False
            else:
                mapping_a[a[i]] = pattern[i]
        return True