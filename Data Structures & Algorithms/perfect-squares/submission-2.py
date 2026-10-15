class Solution:
    def numSquares(self, n: int) -> int:
        res = [float('inf')]* (n+1)
        res[0] = 0
        res[1] = 1
        for i in range(n+1): # for each cell
            for j in range(math.isqrt(i),0,-1):
                if j*j <= i:
                    res[i] = min(res[i],res[i-j*j]+1)
        return res[n]
            