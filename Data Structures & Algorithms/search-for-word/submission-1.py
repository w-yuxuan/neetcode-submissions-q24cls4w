class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        grid = board
        step = [[1,0],[-1,0],[0,-1], [0,1]]
        ROW,COL = len(grid), len(grid[0])
        row, col = ROW-1, COL-1
        visit = set ()

        def dfs(r,c,w):
            if len(word)==w: return True
            for dr,dc in step:
                nr ,nc= r+dr,c+dc
                if 0<= nr <= row and 0<= nc <= col and (nr,nc) not in visit and grid[nr][nc] == word[w]:
                    visit.add((nr,nc))
                    if dfs(nr,nc,w+1):
                        return True
                    visit.discard((nr,nc))
            return False
        
        for x in range(ROW):
            for y in range(COL):
                if grid[x][y]==word[0]:
                    visit.add((x,y))
                    # if len(word)==1:
                    #     return True
                    if dfs(x,y,1):
                        return True
                    visit.discard((x,y))
        return False
