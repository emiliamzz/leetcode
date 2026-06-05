class Solution:
    def isValidColumn(self, board: List[List[str]], index: int) -> bool:
        column = []
        for row in board:
            if row[index] != '.':
                column.append(row[index])
        return len(column) == len(set(column))

    def isValidRow(self, board: List[List[str]], index: int) -> bool:
        row = board[index].copy()
        while '.' in row:
            row.remove('.')
        return len(row) == len(set(row))

    def isValidSquare(self, board: List[List[str]], index: int) -> bool:
        if index < 3:
            square = board[:3]
        elif index < 6:
            square = board[3:6]
        else:
            square = board[6:]
        squares = []
        if index % 3 == 0:
            for i in range(3):
                squares.extend(square[i][:3])
        elif index % 3 == 1:
            for i in range(3):
                squares.extend(square[i][3:6])
        else:
            for i in range(3):
                squares.extend(square[i][6:])
        while '.' in squares:
            squares.remove('.')
        return len(squares) == len(set(squares))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            print(i, board)
            if not self.isValidRow(board, i):
                return False
            if not self.isValidColumn(board, i):
                return False
            if not self.isValidSquare(board, i):
                return False
        return True