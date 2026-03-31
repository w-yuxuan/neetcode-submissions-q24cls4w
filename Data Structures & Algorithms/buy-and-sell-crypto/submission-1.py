class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        i = 0
        j = 1
        while i<j<=len(prices)-1:
            if prices[j]>prices[i]:
                best= max(prices[j]-prices[i],best)
                j+=1
            else: 
                i=j
                j+=1
        return best
