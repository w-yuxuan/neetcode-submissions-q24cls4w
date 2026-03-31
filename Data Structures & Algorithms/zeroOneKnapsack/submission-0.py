#brute force
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        def dfs(i,p,w,c):
            if i == len(profit): return 0
            #skip item i
            curmax = dfs(i+1,p,w,c)
            #include i
            c = c - weight[i] 
            #if at capacity: compare to max
            if c >=0:
                newsum = dfs(i+1,p,w,c) + profit[i]
                curmax = max(curmax,newsum)
            return curmax

        return dfs(0,profit,weight,capacity)
