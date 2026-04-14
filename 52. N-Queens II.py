class Solution:
    def helper(self, board, i):
        if 0 not in board[i]:
            return 0
        if i == len(board) - 1:
            return board[i].count(0)
        count = 0
        for j in range(len(board[i])):
            if board[i][j] == 0:
                new_board = [row[:] for row in board]
                new_board[i][j] = 1
                left = j - 1
                right = j + 1
                for x in range(i + 1, len(board)):
                    if left >= 0:
                        new_board[x][left] = -1
                        left -= 1
                    if right < len(board):
                        new_board[x][right] = -1
                        right += 1
                    new_board[x][j] = -1
                count += self.helper(new_board, i + 1)
        return count

    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        if n < 4:
            return 0
        if n == 4:
            return 2
        board = [[0] * n] * n
        return self.helper(board, 0)