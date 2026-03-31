# redo bottom up case 

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def btu(n):
            if n < 3:
                return n
            if n in cache:
                return cache[n]
            cache[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
            return cache[n]
        return btu(n)
    
