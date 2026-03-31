#fix
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0

        def dfs(visit,r,c,grid):
            nonlocal maxarea,area
            #initialize 
            row = len(grid)-1
            col = len(grid[0])-1
            visit.add((r,c))

            step = [(0, 1), (0, -1), (1, 0), (-1, 0) ]

            for dr, dc in step:
                if r+dr < 0 or c+dc < 0 or r+dr > row or c+dc > col or (r+dr,c+dc) in visit or grid[r+dr][c+dc]==0:
                    continue
                visit.add((r+dr,c+dc))
                visit,area = dfs(visit,r+dr,c+dc,grid)
                area +=1
                #maxarea = max(area,maxarea)
            return visit,area          
            #don't remove
       
        # key: make area an nonlocal var and when dfs is cleaning the grid, don't count island but count num steps cleaner takes
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = 1
                    visit,area = dfs(visit,i,j,grid)
                    maxarea = max(area,maxarea)
        return maxarea