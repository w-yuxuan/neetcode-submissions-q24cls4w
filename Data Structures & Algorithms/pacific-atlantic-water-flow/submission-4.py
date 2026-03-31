class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #start from the edge and run dfs to mark where atl and pac can go to, find common pt at the end 
        h=heights
        row = len(h)-1
        col = len(h[0])-1
        ROW = row+1
        COL = col+1

        visit1,visit2 = set(),set()
        # def storage
        atl = [[False]*COL for _ in range(ROW)]
        pac = [[False]*COL for _ in range(ROW)]
        res = []

        step = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r,c,mem,visit):
            mem[r][c]=True
            visit.add((r,c))
            for dr,dc in step:
                if 0<=r+dr<=row and 0<=c+dc<=col and (r+dr,c+dc) not in visit and h[r+dr][c+dc]>=h[r][c]:
                    dfs(r+dr,c+dc,mem,visit)
            #visit.discard((r,c))
            return 

        for r in range(ROW):
            dfs(r,col,atl,visit1)
            dfs(r,0,pac,visit2)
        for c in range(COL):
            dfs(row,c,atl,visit1)
            dfs(0,c,pac,visit2)
            
        for i in range(ROW):
            for j in range(COL):
                if atl[i][j] and pac[i][j]:
                    res.append((i,j))
        return res

