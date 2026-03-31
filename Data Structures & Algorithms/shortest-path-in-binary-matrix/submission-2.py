class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #initialize val
        length = 1
        row = len(grid)-1 #index of the last item
        col = len(grid[0])-1
        visted = set()
        queue = deque()

    #append the first element to queue if it's not 1
        if grid[0][0]==1 or grid[row][col]==1 : return -1
        visted.add((0,0))
        queue.append((0,0))

        # check if current spot is the end
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == row  and c == col:
                    return length
                att = [(0, 1), (0, -1), (1, 0), (-1, 0),
                    (1, 1), (1, -1), (-1, 1), (-1, -1)]
            #step in8 dir, check if that's a valid step, if yes record inot visted\queue, if not do nothing
                for dr,dc in att:
                    if (r+dr > row or c+dc > col or min(r+dr,c+dc) < 0 or grid[r+dr][c+dc] ==1 or ((r+dr,c+dc) in visted) ):
                        continue
                    visted.add((r+dr,c+dc))
                    queue.append((r+dr,c+dc))
            length+=1
        # return -1 if not found  
        return -1
        