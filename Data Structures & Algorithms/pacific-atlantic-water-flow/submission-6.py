class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        g = heights
        ROW ,COL = len(heights), len(heights[0])
        row, col = ROW-1, COL - 1
        step = [(0,1),(0,-1),(1,0),(-1,0)]
        # tl, br = deque(),deque()
        p,a = set(),set()

        # start bfs from all tl or br cells, add in q 
        for x in range(ROW):
            # tl.append((x,0))
            p.add((x,0))
            # br.append((x,col))
            a.add((x,col))

        for y in range(COL):
            # tl.append((0,y))
            p.add((0,y))
            # br.append((row,y))
            a.add((row,y))
        
        def dfs(r,c,visit):
            visit.add((r,c))
            for dr,dc in step:
                nr,nc = r+dr,c+dc
                if 0<=nr<=row and 0<=nc<=col and g[nr][nc]>=g[r][c] and (nr,nc) not in visit:
                    dfs(nr,nc,visit)
                    # visit.remove((nr,nc))
    
        for i,j in a.copy():
            dfs(i,j,a)
        for i,j in p.copy():
            dfs(i,j,p)
        
        res = []
        for i,j in a:
            if (i,j) in p:
                res.append([i,j])
        return res


        