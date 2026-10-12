class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #at ea 
        grid=heights
        row,col = len(grid)-1,len(grid[0])-1
        ROW,COL = row+1,col+1
        steps = ([0,1],[0,-1],[1,0],[-1,0])
        # steps = ([0,1],[1,0])
        h = [(0,0,0)] #(minEff,x,y,curmax,curmin)
        heapq.heapify(h)
        visit = set()

        while h:
            eff,r,c= heapq.heappop(h)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if r==row and c==col:
                return eff
            for dr,dc in steps:
                nr,nc = r+dr,c+dc
                if 0<=nr<=row and 0<=nc<=col and (nr,nc) not in visit:
                    new = abs(grid[nr][nc]-grid[r][c])
                    heapq.heappush(h,(max(eff,new),nr,nc))
        





