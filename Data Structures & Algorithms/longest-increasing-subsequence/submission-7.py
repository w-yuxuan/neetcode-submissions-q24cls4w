class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [[0]*(len(nums)) for i in range(len(nums))]
        mem[0][0]=1

        for i in range(1,len(nums)): # index of largest prev values
            mem[i][i] = 1
            for j in range(i):  #cur index
                mem[i][j] = mem[i-1][j]
                if nums[i] > nums[j]:
                    mem[i][i] = max(mem[i-1][j]+1,mem[i][i])
        return max(max(row) for row in mem)
                






