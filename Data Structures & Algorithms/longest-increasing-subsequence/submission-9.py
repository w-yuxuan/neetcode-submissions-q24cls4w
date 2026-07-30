class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [[0]*len(nums) for i in range(len(nums))]

        for i in range(len(nums)):
            mem[i][i]=1
            for j in range(i):
                mem[i][j]=mem[i-1][j]
                if nums[i] > nums[j]:
                    mem[i][i]=max(mem[i][i],mem[i-1][j]+1)
        
        return max(max(mem[i] for i in range(len(mem))))