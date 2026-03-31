class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #initialize
        # check if i return 0 or put in (0,0)'s value and register length 1
        length = 1
        visit = set()
        queue = deque()
        row = len(grid)-1  #index of the final corner
        col = len(grid[0])-1
        if grid[0][0] == 1 or grid[row][col] == 1: return -1
        queue.append((0,0))
        visit.add((0,0))

#keep on popping and check if we are at the last corner
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == row and c==col:
                    return length

# each pop, search 8 dir
                att = [(0, 1), (0, -1), (1, 0), (-1, 0),
                    (1, 1), (1, -1), (-1, 1), (-1, -1)]
                for dr,dc in att: #check if we can step there
                    if ((r+dr,c+dc) in visit or r+dr > row or c+dc > col or min(r+dr,c+dc) < 0 or grid[r+dr][c+dc]==1):
                        continue
                    visit.add((r+dr,c+dc))
                    queue.append((r+dr,c+dc))
            length+=1
        return -1
        