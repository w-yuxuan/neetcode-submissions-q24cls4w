class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # if i start from each point and go horizontal / vertical, then it's (m*n)^2
        # yet if i read each row then each col, if i can find 2 of 1 then i append 2
        # and append +1 if i see any more, that is only 2x m*n
        ROW = len(grid)
        COL = len(grid[0])
        res = 0
        row = [0]*ROW
        col = [0]*COL
        
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1:
                    row[r]+=1
                    col[c]+=1
                        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1 and ((row[r]>1) or col[c]>1):
                    res+=1
        return res
 

        