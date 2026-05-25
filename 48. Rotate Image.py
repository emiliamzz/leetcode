class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == j:
                    break
                save = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = save
        for row in matrix:
            row.reverse()