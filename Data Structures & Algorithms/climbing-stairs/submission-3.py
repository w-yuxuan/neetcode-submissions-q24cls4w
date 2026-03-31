class Solution:
    cache = {1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n 
        if n in self.cache:
            return self.cache[n]
        res= self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n]=res
        return res
