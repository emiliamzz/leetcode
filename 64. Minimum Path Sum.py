class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ans = grid[0]
        ans = [ans] * 2
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0:
                    if j != 0:
                        ans[0][j] += ans[0][j-1]
                else:
                    if j == 0:
                        ans[1][j] = ans[0][j] + grid[i][j]
                    else:
                        ans[1][j] = grid[i][j] + min(ans[0][j], ans[1][j-1])
            ans[0] = ans[1]
        return ans[1][-1]