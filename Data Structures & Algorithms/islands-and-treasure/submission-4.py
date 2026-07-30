class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)-1
        col = len(grid[0])-1
        ROW = row+1
        COL = col+1
        q = deque()
        visited = set()
        tar = 2^31-1
        length =1 ## edit since the steps below we take should leave length 1 at the spots we step onto
        steps = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==0:
                    q.append((i,j))
                    visited.add((i,j))
        
        while q:
            for i in range(len(q)): # forgot this line 
                r,c = q.popleft()
                # if grid[r][c]==0:
                
                # no stopping edge cases
                for dr,dc in steps:
                    if 0 <= r+dr <= row and 0<=c+dc<= col and grid[r+dr][c+dc]!=-1 and (r+dr,c+dc) not in visited:
                        q.append((r+dr,c+dc))
                        visited.add((r+dr,c+dc))#forgot 
                        grid[r+dr][c+dc]=length # frogot to write result 
                    # don't need to pop visited ones
            length+=1
        return 
                
            

