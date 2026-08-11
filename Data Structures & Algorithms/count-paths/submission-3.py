class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        buffer = [[0]*n for _ in range(m)]
        for i in range(m):
            buffer[i][0]=1
        for j in range(n):
            buffer[0][j] =1
        for i in range(1,m):
            for j in range(1,n):
                buffer[i][j]+= buffer[i][j-1]+buffer[i-1][j]
        return buffer[m-1][n-1]
                