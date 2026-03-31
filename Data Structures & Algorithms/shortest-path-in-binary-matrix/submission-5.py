# repeat 11/29
#special case: start and ending with [1]
class Solution:
     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #initialize
        row = len(grid)-1 
        col = len(grid[0])-1
        if grid[row][col]==1 or grid[0][0]==1:
            return -1
        visited = set()
        queue = deque()
        length = 1
        queue.append((0,0))
        visited.add((0,0))

        # for each box check if I'm at the end
        # must use range since we will need to use the previous len(queue)
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == row and c == col:
                    return length

                step = [(0, 1), (0, -1), (1, 0), (-1, 0),
                    (1, 1), (1, -1), (-1, 1), (-1, -1)] 
                for dr, dc in step:
                    if ((r+dr > row) or (c+dc > col) or (r+dr <0) or (c+dc<0) or ((r+dr,c+dc) in visited) or (grid[r+dr][c+dc] ==1) ):
                        continue
                    queue.append((r+dr,c+dc))
                    visited.add((r+dr,c+dc))
            length+=1
        return -1 
        # for each box, check if I can go 8 dir
        
