class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        b,s = 0, 1
        p = prices
        best = 0
        while s<= len(p)-1:
            if p[s] <= p[b]:
                b=s
            else:

                best = max(p[s]-p[b],best)
            s+=1
        return best
                
