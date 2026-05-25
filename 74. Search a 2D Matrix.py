class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        row = None
        while high - low > 1:
            mid = round((high - low) / 2) + low
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] > target:
                row = mid
                break
            else:
                low = mid + 1
        if row == None:
            if matrix[low][0] == target:
                return True
            if matrix[low][0] > target:
                return False
            if matrix[high][0] == target:
                return True
            if matrix[high][0] < target:
                row = high
            else:
                row = low
        if row == None:
            return False
        low = 0
        high = len(matrix[row]) - 1
        while high - low > 1:
            mid = round((high - low) / 2) + low
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if matrix[row][low] == target:
            return True
        if matrix[row][high] == target:
            return True
        return False