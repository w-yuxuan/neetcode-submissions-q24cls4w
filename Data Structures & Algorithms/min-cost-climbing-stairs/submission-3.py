class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #best=sum(i for i in cost)
        cache={}
        c=len(cost)
        def find(j):
            if j >= c:
                return 0
            if j in cache:
                return cache[j]
            res=cost[j]+min(find(j+2),find(j+1))
            cache[j]=res
            return res
        return min(find(0),find(1))




