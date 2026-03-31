class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #plan: for each cell, call bfs, initiate length, goal is to find 0 instead of the right corner,append current cell after while loop 
        row = len(grid)-1
        col = len(grid[0])-1
        inf = 2**31-1

        # for each point on the grid i call bfs on, i store the min dist to 0
        def bfs(grid,x,y):
            #initialize
            minL = inf
            l = 0
            visit = set()
            queue = deque()
            #check if we are at target
            #no need to check r,c, they must be inf to be traversed 
            #while dfs' special point is about removing the traversed r,c point
            queue.append((x,y))
            visit.add((x,y))

            while queue:
                for i in range(len(queue)): #don't need this to find r,c pairs
                    r,c = queue.popleft()
                    if grid[r][c] == 0:
                        minL = min(minL,l)

                    step = [(0,1),(0,-1),(1,0),(-1,0)]
                    for dr,dc in step:
                        if r+dr < 0 or c+dc < 0 or r+dr > row or c+dc > col or (r+dr,c+dc) in visit or grid[r+dr][c+dc] == -1:
                            continue
                        queue.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc)) # no need to return visit and input to the next layer, as program will write an l value for that grid point, which is never inf, and effectively told later steps not to call bfs on it
                l+=1
            grid[x][y] = minL
            return grid

        for i in range(row+1):
            for j in range(col+1):
                #if grid[i][j] ==0: grid[i][j] ==0
                if grid[i][j] == inf:
                    grid=bfs(grid,i,j)
        return 
                

