class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        r,c = 0,0
        row = len(grid)-1
        col = len(grid[0])-1  
        ways = 0
        if grid[0][0] ==1 or grid[row][col]==1:return 0      
        
        def dfs(grid,visit,r,c):
            nonlocal ways
            if r == row and c == col:
                ways +=1
            visit.add((r,c))

            step = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr,dc in step:
                if r+dr<0 or c+dc<0 or r+dr>row or c+dc>col or (r+dr,c+dc) in visit or grid[r+dr][c+dc] == 1:
                    continue
                dfs(grid,visit,r+dr,c+dc)
                #visit.remove((r+dr,c+dc)) #you chose a dir, you can't cut to other dir.s and repeate the same loops
            visit.remove((r,c))

        dfs(grid,visit,r,c)
        return ways