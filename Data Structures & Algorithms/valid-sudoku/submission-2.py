class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows: 
        skip = {',','.'}
        for x in range(9):
            r = set()
            for y in range(9): # checks for ea row 
                if board[x][y] in skip:
                    continue
                if board[x][y] in r:
                    return False
                else: r.add(board[x][y]) 
                
        for y in range(9):
            c = set()
            for x in range(9): # checks for ea col
                if board[x][y] in skip:
                    continue 
                if board[x][y] in c:
                    return False   
                else: c.add(board[x][y])         

        beg = []
        for dx in range(0,9,3):
            for dy in range(0,9,3):
                beg.append((dx,dy))

        def check(start):
            x,y = start
            s = set()
            for dx in range(3):
                for dy in range(3):
                    if board[x+dx][y+dy] in skip:
                        continue
                    if board[x+dx][y+dy] in s:
                        return False
                    else: s.add(board[x+dx][y+dy]) 

        for pos in beg:
            if check(pos) == False:
                return False
        
        return True



