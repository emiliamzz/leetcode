class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = []
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0 and j not in cols:
                        cols.append(j)
                matrix[i] = [0] * len(matrix[i])
        for i in range(len(matrix)):
            for j in cols:
                matrix[i][j] = 0