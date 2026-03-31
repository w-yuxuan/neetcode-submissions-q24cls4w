class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n = len(nums)
        def df(i):# return num steps 
            store = float('inf')
            if i>=n-1:
                return 0
            for j in range(1,nums[i]+1):# num steps that i can advance
                store = min(store,df(i+j)+1)
            return store
        return df(0)


