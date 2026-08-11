class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROW,COL = m,n
        row,col = m-1,n-1

        step = [[1,0],[0,1]]
        memo = {}
        # visit.add()
        
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            res = 0
            if r==row and c == col:
                return 1
        
            for dr,dc in step:
                nc = c+dc
                nr = r+dr
                if 0<=nr<=row and 0<=nc<=col: 
                    res+=dfs(nr,nc)
            memo[(r,c)] = res
            return res
        return dfs(0,0)