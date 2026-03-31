class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])
        length = 1
        queue=deque()
        visit=set()
        if grid[0][0] == 1: return -1
        queue.append((0,0))
        visit.add((0,0))

        while queue:
            #check if we are at the target, else we dont finish and pop left
            for spot in range(len(queue)):
                r,c = queue.popleft() 

                if grid[r][c]==0 and r == row-1 and c == col-1:
                    #added to handle if I only have one element: ensure 0, not a 1 
                    return length          
            
                att=[[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[1,1],[1,-1],[-1,1]]
                for dr,dc in att:
                    if (min(r+dr,c+dc)<0 or r+dr >= row or c+dc >= col or grid[r+dr][c+dc] == 1 or ((r+dr,c+dc) in visit)):
                        continue
                    queue.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))

            length+=1
        return -1
        