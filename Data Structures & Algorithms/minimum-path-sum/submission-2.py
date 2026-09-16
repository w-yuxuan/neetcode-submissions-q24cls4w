class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW,COL = len(grid), len(grid[0])
        dp = [[float('inf')]*COL for i in range(ROW)]
        row,col = ROW-1,COL-1

        dp[0][0]=grid[0][0]
        for r in range(ROW):
            for c in range(COL):
                if r > 0:
                    dp[r][c] = min(dp[r][c],dp[r-1][c]+grid[r][c])
                    
                if c > 0 : 
                    dp[r][c] = min(dp[r][c],dp[r][c-1]+grid[r][c])

        return dp[ROW-1][COL-1]