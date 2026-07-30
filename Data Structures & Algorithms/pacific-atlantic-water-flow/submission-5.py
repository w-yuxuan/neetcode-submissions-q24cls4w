class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs mxn x 4mn, bfs mxn
        g = heights
        ROW ,COL = len(heights), len(heights[0])
        row, col = ROW-1, COL - 1
        step = [(0,1),(0,-1),(1,0),(-1,0)]
        tl, br = deque(),deque()
        p,a = set(),set()

        # start bfs from all tl or br cells, add in q 
        for x in range(ROW):
            tl.append((x,0))
            p.add((x,0))
            br.append((x,col))
            a.add((x,col))

        for y in range(COL):
            tl.append((0,y))
            p.add((0,y))
            br.append((row,y))
            a.add((row,y))
        
        def bfs(q,visit):
            while q:
                r,c = q.popleft()
                for dr,dc in step:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<=row and 0<=nc<=col and (nr,nc) not in visit and g[r][c]<=g[nr][nc]:
                        visit.add((nr,nc))
                        q.append((nr,nc))
        bfs(tl,p)
        bfs(br,a)

        res = []
        for i,j in p:
            if (i,j) in a:
                res.append([i,j])
        return res

  
