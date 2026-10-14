class Solution:
    def numSquares(self, n: int) -> int:
        mem = {}
        def dfs(p):
            if p in mem:
                return mem[p]
            if p==0:
                return 0
   
            # res = 0
            if p == 1:
                return 1

            res = float('inf')
            for i in range(int(math.isqrt(p)),0,-1):
                if i*i <= p:
                    res = min(res, dfs( p - i*i) + 1)
            mem[p]=res

            return res
        return dfs(n)
