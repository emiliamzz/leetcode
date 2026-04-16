class Solution:
    def helper(self, word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
            if count > 1:
                return False
        return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if self.helper(beginWord, endWord):
            return 2
        if beginWord in wordList:
            wordList.remove(beginWord)
        count = 2
        layer = [beginWord]
        while len(layer) > 0:
            new_layer = []
            for word in layer:
                if self.helper(word, endWord):
                    return count
                new_wordList = []
                for new_word in wordList:
                    if self.helper(word, new_word):
                        new_layer.append(new_word)
                    else:
                        new_wordList.append(new_word)
                wordList = new_wordList
            layer = new_layer
            count += 1
        return 0