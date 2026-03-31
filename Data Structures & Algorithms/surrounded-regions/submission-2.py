class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # same as islands: find all o to. start a bfs/dfs to clear them to x
        # but need to add something to check that they are surrounded on 4 sides
        # i can hold off changing o to x until i verify that non of the o is on the edge!
        # just add them to a list cur to change to x after the program stops
        ROW = len(board)
        COL = len(board[0])
        row = ROW -1
        col = COL -1
        q = deque()
        visited= set()
        step = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(x,y):
            clean = [] # clean up list after each exploration dir
            clean.append((x,y))

            isclean = True
            while q:
                for i in range(len(q)):
                    x,y = q.popleft()
                    for dx,dy in step:
                        if 0<=x+dx<=row and 0<=y+dy<=col and (x+dx,y+dy) not in visited and board[x+dx][y+dy]=='O':
                            clean.append((x+dx,y+dy))
                            visited.add((x+dx,y+dy)) #even if O is later found to be next to edge, don't go there again since it's connected to an exit route
                            #but add q only when 
                            q.append((x+dx,y+dy))
                            if (x+dx ==0 or x+dx ==row or y+dy == 0 or y+dy ==col):
                                isclean=False
            if isclean:
                for xx,yy in clean:
                    board[xx][yy]='X'       
            return 
                    
        for r in range(1,row): # not ROW COL , to not search the edges
            for c in range(1,col):
                if board[r][c] == 'O' and (r,c) not in visited:
                    q.append((r,c)) 
                    visited.add((r,c))
                    bfs(r,c)
        return 





