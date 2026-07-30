class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [ ]
        store  = deque([[]])
        # s = set ()

        # def dfs(cur):
        l = 0 # cur's len
        n=len(nums)
        
        # for i in range(n):
        for i in nums:
            for _ in range(len(store)):
                s = store.popleft().copy()
                for j in range(l+1):
                    new = s.copy()
                    new.insert(j,i)
                    store.append(new)
            l+=1
        return list(store)
                


        # dfs([])