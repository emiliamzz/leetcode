class Solution:
    def numNeighbors(self, board, x, y):
        count = 0
        live = [1, 2]
        if x != 0:
            if board[x-1][y] in live:
                count += 1
            if y != 0:
                if board[x-1][y-1] in live:
                    count += 1
            if y != len(board[x]) - 1:
                if board[x-1][y+1] in live:
                    count += 1
        if y != 0:
            if board[x][y-1] in live:
                count += 1
        if y != len(board[x]) - 1:
            if board[x][y+1] in live:
                count += 1
        if x != len(board) - 1:
            if board[x+1][y] in live:
                count += 1
            if y != 0:
                if board[x+1][y-1] in live:
                    count += 1
            if y != len(board[x]) - 1:
                if board[x+1][y+1] in live:
                    count += 1
        return count

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0 1 - initial and unchanged states
        # 2 - was 1, should become 0
        # 3 - was 0, should become 1
        # can do lambda function afterwards to do -2 to all changed
        for i in range(len(board)):
            for j in range(len(board[i])):
                count = self.numNeighbors(board, i, j)
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 2
                elif board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
        for i in range(len(board)):
            board[i] = list(map(lambda x: x - 2 if x > 1 else x, board[i]))
