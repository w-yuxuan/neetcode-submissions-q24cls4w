class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        # visit.add((0,0))
        # no need to check if 00 is traversable
        
        # no need for queue
        row = len(grid)-1
        col = len(grid[0])-1
        ways = 0
        step = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(visit,r,c):
            nonlocal ways
            visit.add((r,c))
            if r==row and c==col:
                ways+=1

            for dr,dc in step:
                if 0<=r+dr<=row and 0<=c+dc<=col and (r+dr,c+dc) not in visit and grid[r+dr][c+dc]!=1:
                    dfs(visit,r+dr,c+dc)
            visit.remove((r,c))
        if grid[0][0]==0:
            dfs(visit,0,0)
        else: return 0
        return ways
        