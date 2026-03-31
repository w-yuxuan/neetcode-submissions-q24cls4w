class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        mem = [float('inf') ]*len(nums)
        mem[0]=0
        # i = 0
        n=len(nums)
        for i in range(n):
            for j in range(1,nums[i]+1): #nums steps i can advance from i
                if i+j > n-1:
                    break
                mem[i+j] = min(mem[i+j],mem[i]+1)
           
        return mem[-1]

