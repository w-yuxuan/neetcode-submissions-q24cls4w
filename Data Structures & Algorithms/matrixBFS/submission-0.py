class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        #initialize param
        col = len(grid[0]) -1
        row = len(grid) - 1
        visit = set()
        queue = deque()
        length = 0
        if grid[row][col] == 1 or grid[0][0]==1: return -1
        queue.append((0,0))
        visit.add((0,0))

        # while loop to check if you are at the end cell
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == row and c == col:
                    return length

                dir = [(1,0),(-1,0),(0,1),(0,-1)] #,(1,1),(-1,-1),(-1,1),(1,-1)]
            #for each cell, try all 4/8 dir
                for dr,dc in dir:
                    if r+dr < 0 or c+dc <0 or r+dr > row or c+dc > col or (r+dr,c+dc) in visit or grid[r+dr][c+dc]==1:
                        continue
                    queue.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))
            length+=1    
        return -1


        #block out visited

