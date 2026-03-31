class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s =sum(stones)
        goal = s//2
        total = 0
        cache = {}
        def dfs(i,total):
            # if total == goal:
            #     cache[(i,total)] = 0
            #     return 0 # can further calc but their min would be 0
            if i > len(stones)-1:
                return abs(abs(s-total)-total) # abs(other side - this side)

            if (i,total) in cache:
                return cache[(i,total)]
            cache[(i,total)]=min(dfs(i+1,total+stones[i]),dfs(i+1,total))
            return cache[(i,total)]
        return dfs(0,0)
            