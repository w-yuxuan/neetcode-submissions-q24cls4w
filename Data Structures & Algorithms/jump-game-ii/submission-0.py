class Solution:
    def jump(self, nums: List[int]) -> int:
        mem = [float('inf')] * len(nums)
        mem[-1]=0

        def dfs(i):
            if i>=len(nums)-1:
                # mem[i]=0
                return 0
            if mem[i]!=float('inf'):
                return mem[i]
            # for n in range(len(nums)-2,-1,-1):
            cur_min = float('inf') 
            for n in range(1,nums[i]+1):
                cur_min = min(dfs(i+n)+1,cur_min)
            mem[i] = cur_min
            return mem[i]
        return dfs(0)

                
