class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board) -1
        ROW = row+1
        col = len(board[0])-1
        COL = col+1

         # check if i can visit first/last val
        visit = set()
        q = deque()
        step = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c,visit):
            for dr,dc in step:
                if 0<=r+dr<=row and 0<=c+dc<=col and board[r+dr][c+dc] == 'O' and (r+dr,c+dc) not in visit:
                    visit.add((r+dr,c+dc))
                    dfs(r+dr,c+dc,visit)
            #visit.discard((r,c))

        # mark all O that i can reach from the edges as visited, do nothing on them. Then search for all other O, mark them X
        for j in range(COL):
            if board[0][j] == 'O':
                visit.add((0,j))
                dfs(0,j,visit)

                
            if board[row][j] == 'O':
                visit.add((row,j))
                dfs(row,j,visit)
                

        for i in range(ROW):
            if board[i][0] == 'O':
                visit.add((i,0))
                dfs(i,0,visit)
                
                
            if board[i][col] == 'O':
                visit.add((i,col))
                dfs(i,col,visit) 
                       
        
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'O' and (i,j) not in visit:
                    board[i][j] = 'X'

        
        return  