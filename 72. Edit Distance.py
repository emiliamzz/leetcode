class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        chart = [[]]
        for i in range(len(word2)+1):
            chart[0].append(i)
        for j in range(1, len(word1)+1):
            chart.append([j])
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    chart[i].append(chart[i-1][j-1])
                else:
                    chart[i].append(min(chart[i-1][j-1], chart[i-1][j], chart[i][j-1]) + 1)
        return chart[-1][-1]