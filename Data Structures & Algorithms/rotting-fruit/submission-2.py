class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #opt1: land on rottens one by one like the islands prob
        #opt2: land simultaneously on all rotten and spread until no more to spread, then check if there are remaining1 in for loop

        #bfs count 
        
        #initialize:
        q = deque()
        visit = set()
        row = len(grid)-1
        ROW = row +1
        col = len(grid[0])-1
        COL = col +1
        t=-1
        fresh=0
        #no need to check if  corners can be traversed
        #def bfs(r,c,visited,q):
        step = [(1,0),(-1,0),(0,1),(0,-1)]
    
        #initial scan
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visit.add((i,j))
                elif grid[i][j] ==1:
                    fresh +=1
                
        #if not q: return 0     # fixes [[0]] but breaks [[1]]  : both not q but return 0 and -1, respectively  
        if fresh==0:return 0          
        #check when loop end : all neighbors are not 1

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                #if grid[r][c]!=1:
                #    continue

                for dr,dc in step:
                    if 0<=r+dr<=row and 0<=c+dc<=col and (r+dr,c+dc) not in visit and grid[r+dr][c+dc]==1:
                        q.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))
                        grid[r+dr][c+dc]=2
            t+=1
        #final scan: should be only 2 and 0 left, if there's 1 = frsh froot left then impossible to rot all 
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1: return -1
                #can't check [[0]] here since there's often [0] left after rotting all of them
        return t 
                        
                    

