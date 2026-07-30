class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        ROW = len(grid)
        COL = len(grid[0])
        row,col = ROW-1,COL-1
        visited = set()
        dist = 1
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        step = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            for k in range(len(q)):
                
                r,c = q.popleft()

                for dr,dc in step:
                    if 0<=r+dr<=row and 0<=c+dc<=col and ((r+dr,c+dc) not in visited) and grid[r+dr][c+dc]==2147483647:
                        visited.add((r+dr,c+dc))
                        grid[r+dr][c+dc]=dist
                        q.append((r+dr,c+dc))
            dist+=1
        
