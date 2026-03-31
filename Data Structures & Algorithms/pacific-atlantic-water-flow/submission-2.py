class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #use an external memory sheet to record where i've been to so i don't need sets
        #use a queue 
        col = len(heights[0])-1
        row = len(heights)-1

        atl = [[False]*(col+1) for i in range(row+1)] #can't use (): needs flipping!
        pac = [[False]*(col+1) for i in range(row+1)]

        qa,qp = deque(),deque()

        for r in range(row+1):
            qa.append((r,col))
            qp.append((r,0))
        for c in range(col+1):
            qa.append((row,c))
            qp.append((0,c))

        step = [(0,1),(0,-1),(1,0),(-1,0)]
        # edge always gets water in so no need to check

        def bfs(ocean,grid,q):
            #no need to check if at the target cell
            while q:
                for i in range(len(q)):
                    x,y = q.popleft()
                    ocean[x][y] = True

                    #add to q if allowed
                    for dx,dy in step:
                        if 0<=x+dx<=row and 0<=y+dy<=col and grid[x+dx][y+dy]>=grid[x][y] and ocean[x+dx][y+dy]!=True:
                            q.append((x+dx,y+dy))
                            ocean[x+dx][y+dy] = True
        
        bfs(atl,heights,qa)
        bfs(pac,heights,qp)

        res = []
        for i in range(row+1):
            for j in range(col+1):
                if atl[i][j]==pac[i][j]==True:
                    res.append((i,j))
        return res
