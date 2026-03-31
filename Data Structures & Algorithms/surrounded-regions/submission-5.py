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

        # mark all O that i can reach from the edges as visited, do nothing on them. Then search for all other O, mark them X
        for j in range(COL):
            if board[0][j] == 'O':
                q.append((0,j))
                visit.add((0,j))
                
            if board[row][j] == 'O':
                q.append((row,j))
                visit.add((row,j))

        for i in range(ROW):
            if board[i][0] == 'O':
                q.append((i,0))
                visit.add((i,0))
                
            if board[i][col] == 'O':
                q.append((i,col)) 
                visit.add((i,col))       

        while q:
            r,c = q.popleft()
            # no edge case to stop
            for dr,dc in step:
                if 0<=r+dr<=row and 0<=c+dc<=col and board[r+dr][c+dc] == 'O' and (r+dr,c+dc) not in visit:
                    visit.add((r+dr,c+dc))
                    q.append((r+dr,c+dc))
        
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'O' and (i,j) not in visit:

                    board[i][j] = 'X'

        
        return  
                  

                    

            
