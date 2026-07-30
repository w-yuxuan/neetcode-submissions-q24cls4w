class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # if i start from each point and go horizontal / vertical, then it's (m*n)^2
        # yet if i read each row then each col, if i can find 2 of 1 then i append 2
        # and append +1 if i see any more, that is only 2x m*n
        ROW = len(grid)
        COL = len(grid[0])
        res = 0
        s = set()
        
        
        for r in range(ROW):
            tot = 0
            lst=deque()
            for c in range(COL):
                if grid[r][c]==1:
                    tot+=1 #count this row/col 1's first 
                    lst.append((r,c))
                if tot>=2: # if we do have more than 2 then they should be added to set
                    for r1,c1 in lst:
                        s.add((r1,c1))
                    
            if tot>=2:res+=tot
        
        for c in range(COL):
            tot = 0
            lst = deque()
            for r in range(ROW):
                if grid[r][c]==1:
                    tot+=1 #count this row/col 1's first 
                    lst.append((r,c))
                if tot>=2: # if we do have more than 2 then they should be added to set
                    for r1,c1 in lst:
                        s.add((r1,c1))
            if tot>=2:res+=tot
        return len(s)

        