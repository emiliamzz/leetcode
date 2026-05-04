class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            x = list(word)
            x.sort()
            sort = "".join(x)
            if sort in anagrams:
                anagrams[sort].append(word)
            else:
                anagrams[sort] = [word]
        output = []
        for anagram in anagrams:
            output.append(anagrams[anagram])
        return output