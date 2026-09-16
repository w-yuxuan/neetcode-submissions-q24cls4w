class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mem = {}
        mem[(0,0)] = grid[0][0]
        ROW,COL = len(grid),len(grid[0])
        def dfs(r,c):
            res = float('inf')
            if (r,c) in mem:
                return mem[(r,c)]
            if r>0:
                res = min(res,dfs(r-1,c)+grid[r][c])
            if c>0:
                res = min(res,dfs(r,c-1)+grid[r][c])
            mem[(r,c)] = res 
            return res           
        return dfs(ROW-1,COL-1)









