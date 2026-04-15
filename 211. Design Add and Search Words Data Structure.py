class WordDictionary:
    def __init__(self):
        self.dictionary = {}

    def addWord(self, word: str) -> None:
        length = str(len(word))
        first = word[0]
        if length in self.dictionary:
            if first in self.dictionary[length]:
                self.dictionary[length][first].append(word)
            else:
                self.dictionary[length][first] = [word]
        else:
            self.dictionary[length] = {}
            self.dictionary[length][first] = [word]

    def search(self, word: str) -> bool:
        length = str(len(word))
        if length not in self.dictionary:
            return False
        words = self.dictionary[length]
        first = word[0]
        if first == '.':
            for x in words:
                for item in words[x]:
                    if re.search(word, item):
                        return True
            return False
        if first not in words:
            return False
        for item in words[first]:
            if re.search(word, item):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)