# fix dfs 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        
        def dfs(visit,r,c,grid):
            #initialize
            row = len(grid)-1
            col = len(grid[0])-1
            #comp to bfs, no queue, just backtrack after you go to each point and search 4 dir 
            #at each point, explore 4 dir

            if not visit:
                visit = set()
            #leave foot print
            visit.add((r,c))
            grid[r][c]= "0"
            
            dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr,dc in dir:
                if r+dr < 0 or c+dc < 0 or r+dr > row or c+dc > col or (r+dr,c+dc) in visit or grid[r+dr][c+dc] == "0" :
                    continue
                visit = dfs(visit,r+dr,c+dc,grid)
                #visit.add((r+dr,c+dc))
                #grid[r+dr][c+dc] =0 # that step's dfs will fix it 

            #visit.remove((r,c)) # don't forget innner ()      

            return visit
        

        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    visit = dfs(visit,i,j,grid)
                    islands += 1

        return islands
                