#repeat brute force
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dfs(i,p,c):#returns max profit
            #edge case
            if i == len(profit):
                return 0
            #don't take in
            maxprofit = dfs(i+1,p,c)
            #take in, check if can
            c = c-weight[i]
            if c >=0:
                cur = dfs(i+1,p,c) + p[i]
                maxprofit = max(maxprofit,cur)
            return maxprofit
            
        return dfs(0,profit,capacity)
