class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        step = [(0,1),(1,0),(0,-1),(-1,0)]
        ROW = len(grid)
        COL = len(grid[0])
        row = ROW -1
        col = COL -1
        p = 0
        if grid[0][0]==1 or grid[row][col]==1:
            return 0
        def dfs(visit,r,c):
            
            nonlocal p #forgot
            visit.add((r,c)) # forgot
            if r == row and c==col:
                p+=1
            for dr,dc in step:
                if 0<=r+dr<=row and 0<=c+dc<=col and grid[r+dr][c+dc]!=1 and (r+dr,c+dc) not in visit:
                    visit.add((r+dr,c+dc))
                    dfs(visit,r+dr,c+dc)
            visit.remove((r,c))
        dfs(visit,0,0)
        return p