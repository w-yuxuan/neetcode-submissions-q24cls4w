class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[0]*n for i in range(m)]
        # mem[m-1][n-1] = 1
        mem[0][0]=1 # invert the map, no harm sine all points are the same, so that we can walk forward

        # def dfs(r,c):
        #     if r==m-1 and c == n-1:
        #         return 0
        #     mem[r+1][c]+=mem[r][c]
        #     mem[r][c+1]+=mem[r][c]

        for r in range(0,m):
            for c in range(0,n):
                if r+1<m:
                    mem[r+1][c]+=mem[r][c]
                if c+1 < n:
                    mem[r][c+1]+=mem[r][c]
        return mem[m-1][n-1]
