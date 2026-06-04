class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        while len(matrix) > 0:
            # right to left
            spiral.extend(matrix[0])
            if len(matrix) == 1:
                break
            matrix = matrix[1:]
            # top to bottom
            if len(matrix[0]) == 1:
                for row in matrix:
                    spiral.append(row[0])
                break
            for i in range(len(matrix)):
                spiral.append(matrix[i][-1])
                matrix[i] = matrix[i][:-1]
            # left to right
            row = matrix[-1]
            row.reverse()
            spiral.extend(row)
            if len(matrix) == 1:
                break
            matrix = matrix[:-1]
            # bottom to top
            if len(matrix[0]) == 1:
                for i in range(len(matrix)-1, -1, -1):
                    spiral.append(matrix[i][0])
                break
            for i in range(len(matrix)-1, -1, -1):
                spiral.append(matrix[i][0])
                matrix[i] = matrix[i][1:]
        return spiral