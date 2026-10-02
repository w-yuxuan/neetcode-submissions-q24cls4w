class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROW,COL = len(heights), len(heights[0])
        grid = heights
        row,col = ROW-1,COL-1
        # once reach end add to res
        # new node you see: get it out 
        h = [(0,0,0)]
        heapq.heapify(h)
        res = float('inf')
        step = [(0,1),(1,0),(-1,0),(0,-1)]
        visit =set()
        # visit.add((0,0))

        while h:
            e,r,c = heapq.heappop(h)
            if (r,c) in visit:
                continue
            visit.add((r,c))

            if (r,c) == (row,col):
                res = min(res,e)
                return res
            
            for dr,dc in step:
                nr,nc = r+dr,c+dc
                if 0<=nr<=row and 0<=nc<=col and (nr,nc) not in visit:
                    cur = max(abs(heights[nr][nc]-heights[r][c]),e)
                    heapq.heappush(h,(cur,nr,nc))
        return res
        