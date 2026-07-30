class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROW = len(grid)
        COL = len(grid[0])
        row,col = ROW-1,COL-1
        visited = set()
        q= deque()

        step = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]=='1':
                    # visited.add((i,j))
                    q.append((i,j))

        def dfs(r,c):
            for dr,dc in step:
                nr = r+dr
                nc = c+dc
                if 0<=nr<=row and 0<=nc<=col and (nr,nc) not in visited and grid[nr][nc]=='1':
                    visited.add((nr,nc))
                    dfs(nr,nc)
                    # visited.discard(nr,nc)

        for r,c in q:
            if (r,c) not in visited:
                res+=1
                visited.add((r,c))
                dfs(r,c)
                

        return res

    



