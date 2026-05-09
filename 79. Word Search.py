class Solution:
    def search(self, board, seen, word, last):
        if not last:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        if len(word) == 1:
                            return True
                        seen[i][j] = 1
                        if self.search(board, seen, word[1:], [i, j]):
                            return True
                        seen[i][j] = 0
            return False
        i = last[0]
        j = last[1]
        if i > 0 and seen[i-1][j] != 1 and board[i-1][j] == word[0]:
            if len(word) == 1:
                return True
            seen[i-1][j] = 1
            if self.search(board, seen, word[1:], [i-1, j]):
                return True
            seen[i-1][j] = 0
        if j < len(board[0]) - 1 and seen[i][j+1] != 1 and board[i][j+1] == word[0]:
            if len(word) == 1:
                return True
            seen[i][j+1] = 1
            if self.search(board, seen, word[1:], [i, j+1]):
                return True
            seen[i][j+1] = 0
        if i < len(board) - 1 and seen[i+1][j] != 1 and board[i+1][j] == word[0]:
            if len(word) == 1:
                return True
            seen[i+1][j] = 1
            if self.search(board, seen, word[1:], [i+1, j]):
                return True
            seen[i+1][j] = 0
        if j > 0 and seen[i][j-1] != 1 and board[i][j-1] == word[0]:
            if len(word) == 1:
                return True
            seen[i][j-1] = 1
            if self.search(board, seen, word[1:], [i, j-1]):
                return True
            seen[i][j-1] = 0
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = []
        for x in board:
            seen.append([0] * len(board[0]))
        return self.search(board, seen, word, None)