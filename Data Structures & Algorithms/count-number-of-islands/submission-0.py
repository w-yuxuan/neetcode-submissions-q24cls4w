# fix test 2
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def bfs(grid,i,j):
            #for every 1 you can find in all 8 dir starting that point, flip it to 0
            #initialize
            row = len(grid)-1 
            col = len(grid[0])-1
            visit = set()
            queue=deque()
            visit.add((i,j))
            queue.append((i,j))

            # loop over
            while queue:
                #check if we need to stop since we are at the bottom corner is not needed
                #since we are going to all 4 dir
                
                for i in range(len(queue)):
                    r,c = queue.popleft()
                #    if r==row and c == col:
                #        return 
                    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    for dr, dc in dir:
                        if ((r+dr) < 0 or (c+dc) < 0 or (r+dr) > row or (c+dc) > col or grid[r+dr][c+dc] == "0" or (r+dr,c+dc) in visit):
                            continue
                        queue.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))
                        grid[r+dr][c+dc] = "0"
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands +=1
                    bfs(grid,i,j)
        return islands