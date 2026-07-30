class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        row,col = ROW -1, COL -1
        visit = set()
        q = deque()
        area = 0
        
        step = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(x,y):
            q.append((x,y))
            a = 1
            while q:
                
                for i in range(len(q)):
                    r,c = q.popleft()

                    for dr,dc in step:
                        nr ,nc = r+dr,c+dc 
                        if 0<=nr<=row and 0<=nc<=col and (nr,nc) not in visit and grid[nr][nc]==1:
                            grid[nr][nc]=0
                            q.append((nr,nc))
                            a+=1
            return a

        
        
        for x in range(ROW):
            for y in range(COL):
                if grid[x][y]==1:
                    visit.add((x,y))
                    area = max(area,bfs(x,y))
                    
            # area = max(area,a)

        return area
            



        # def dfs(r,c):
        #     nonlocal area
        #     a = 1
        #     for dr,dc in step:
        #         nr ,nc = r+dr,c+dc 
        #         if 0<=nr<=row and 0<=nc<=col and (nr,nc) not in visit and grid[nr][nc]==1:
        #             grid[nr][nc]=0
        #             visit.add((nr,nc))
        #             a+=dfs(nr,nc)
        #     area = max(area,a)
        #     return a
        
        # for i in range(ROW):
        #     for j in range(COL):
        #         if grid[i][j] ==1:
        #             visit.add((i,j))
        #             q.append((i,j))
        #             dfs(i,j)
        # return area


