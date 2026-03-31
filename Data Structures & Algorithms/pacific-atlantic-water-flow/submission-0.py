class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # i can try to flow water from every point, bfs, and only step if neighbors are not taller
        #can keep separate score for p and a
        #find common elements and append to result [ ]
        row = len(heights)-1
        col = len(heights[0])-1

        sP = set()
        qP = deque()
        sA = set()
        qA = deque()
#        for y in set{0,row}:
#            for x in set{0,col}:
        for x in range(row+1):
            qP.append((x,0))
            sP.add((x,0))
            qA.append((x,col))
            sA.add((x,col))
        for y in range(col+1):
            sP.add((0,y))
            qP.append((0,y))
            sA.add((row,y))
            qA.append((row,y))
                #no need to check if allowed to step on 1st point

        #2 options: modify the grid in place to -1 and -2 to denote it has been flooded twice
        # or use 2 sets of  visit , queue pairs to find unions

        while qA:
            for i in range(len(qA)):
                r,c = qA.popleft()

                step = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in step:
                    if r+dr < 0 or c+dc < 0 or r+dr > row or c+dc > col or heights[r+dr][c+dc]<heights[r][c] or (r+dr,c+dc) in sA:
                        continue
                    qA.append((r+dr,c+dc))
                    sA.add((r+dr,c+dc))
        

        while qP:
            for i in range(len(qP)):
                r,c = qP.popleft()

                step = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in step:
                    if r+dr < 0 or c+dc < 0 or r+dr > row or c+dc > col or heights[r+dr][c+dc]<heights[r][c] or (r+dr,c+dc) in sP:
                        continue
                    qP.append((r+dr,c+dc))
                    sP.add((r+dr,c+dc))
        res = []
        for el in sP:
            if el in sA:
                res.append(list(el))
        return res
                    


