class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visit = set()
        row = len(grid)-1
        col = len(grid[0])-1
        ROW,COL = row +1, col+1
        step = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def dfs(r,c):
            nonlocal res
            # q = deque([(i,j)])
            grid[r][c]="0"
 
            # while q:
                # r,c = q.popleft()
                # prune if we are at the corner
            for dr,dc in step:
                if 0<=r+dr<=row and 0<=c+dc<=col and (r+dr,c+dc) not in visit and grid[r+dr][c+dc]=="1":
                    # q.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))
                    # grid[r+dr][c+dc]="0" 
                    dfs(r+dr,c+dc)
                    # grid[r+dr][c+dc]="0" 
                    # visit.remove((r+dr,c+dc))
            return 
        
        for i,item in enumerate(grid):
            for j,num in enumerate(item):
                if num=="1":
                    dfs(i,j)
                    res+=1
        return res