class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        visit = set()
        q = deque()
        ROW = len(grid)
        COL = len(grid[0])
        row = ROW -1
        col = COL-1
        step = [(0,1),(1,0),(0,-1),(-1,0)]
        #check if we can get started even
        if grid[0][0] == 1 or grid[row][col] ==1:
            return -1
        q.append((0,0))
        vist = set([0,0])
        l = 0

        #check base case: we at finish line
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if r == row and c == col:
                    return l
                
                for dr, dc in step :
                    if 0<=r+dr<=row and 0<=c+dc<=col and (r+dr,c+dc) not in visit and grid[r+dr][c+dc] != 1:
                        q.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))
            l += 1
        return -1
        
            