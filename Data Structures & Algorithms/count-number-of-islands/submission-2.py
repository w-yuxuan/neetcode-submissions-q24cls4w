class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        def bfs(i,j):
            nonlocal res
            q = deque([(i,j)])
            visit = set()
            row = len(grid)-1
            col = len(grid[0])-1
            ROW,COL = row +1, col+1
            step = [(1,0),(-1,0),(0,1),(0,-1)]
            
            while q:
                r,c = q.popleft()
                # prune if we are at the corner
                for dr,dc in step:
                    if 0<=r+dr<=row and 0<=c+dc<=col and (r+dr,c+dc) not in visit and grid[r+dr][c+dc]=="1":
                        q.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))
                        grid[r+dr][c+dc]="0" 
            return 
        
        for i,row in enumerate(grid):
            for j,num in enumerate(row):
                if num=="1":
                    bfs(i,j)
                    res+=1
        return res