class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        row = len(grid)-1
        col = len(grid[0])-1
        ROW,COL = row+1,col+1
        step = [(1,0),(-1,0),(0,1),(0,-1)]
        visit = set()

        
        def dfs(r,c):
            visit.add((r,c))#bfs don't need bc it will never go back to the same position, while the dfs set is only for the current path
            grid[r][c]=="0"
            for dr,dc in step:
                if 0<=r+dr<=row and 0<=c+dc<=col and (r+dr,c+dc) not in visit and grid[r+dr][c+dc]=="1":
                    visit.add((r+dr,c+dc))
                    grid[r+dr][c+dc]="0" # like the visit, add it first
                    dfs(r+dr,c+dc)
                    # don't need to remove as we shouldn't come back. we only pop if we want to account for all possible routes.
            return 


        for i,item in enumerate(grid):
            for j,num in enumerate(item):
                if num=="1":
                    dfs(i,j)
                    res+=1
        return res