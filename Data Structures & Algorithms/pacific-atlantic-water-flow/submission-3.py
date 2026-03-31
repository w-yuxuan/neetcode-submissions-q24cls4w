class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #add all pacific cells to queue, see if they can go into atlantic, then add everything in the path to res
        
        h=heights
        res = []
        qp,qa = deque(), deque()
        visit = set()

        row = len(h)-1
        col = len(h[0])-1
        ROW,COL = row+1,col+1

        atl = [[False]*COL for i in range(ROW)]
        pac = [[False]*COL for i in range(ROW)]

        # if row == 0 or col ==0: #only 1 row/col,without this we will add ea point to queue twice 
            # return all points in heights 

        for c in range(COL):
            qp.append((0,c))
            qa.append((row,c))

        for r in range(ROW):
            qp.append((r,0))
            qa.append((r,col))
        
        #prune before add to queue, while dfs needs to add then pop 
        step = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(q,mem):
            while q:
                # temp = [] # i can't pass the currently traversed points bc we are not recursing
                #edge case to stop?
                r,c = q.popleft()
                # if r == row or c == col or r==0 or c==0:
                mem[r][c]=True
                    # don't reutnr keep popping, else the code would end right when it pops the first level of nodes

                for dr,dc in step:
                    if 0<=(r+dr)<=row and 0<=(c+dc)<=col and h[r+dr][c+dc]>= h[r][c] and (r+dr,c+dc) not in visit:
                        q.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))
        bfs(qp,pac)
        visit = set()
        bfs(qa,atl)
        for i in range(ROW):
            for j in range(COL):
                if atl[i][j]==pac[i][j]==True:
                    res.append((i,j))
        return res
        #method 1: start from pacific then atlantic, only add their common subset to the fianl res

