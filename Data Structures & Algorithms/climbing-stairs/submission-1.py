class Solution:
    def climbStairs(self, n: int) -> int:
        k = n//2
        sum = 0
        t = 0
        if n%2!=0: #odd number
            t = 1 #dp
        while k >= 1:
            sum += math.comb(k+t,k)
            k-=1
            t+=2
        return sum+1 # for all 1 case