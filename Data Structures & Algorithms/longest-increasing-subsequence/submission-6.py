class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [0]*len(nums)
        for i in range(len(nums)):
            res = 1
            for j in range(i-1,-1,-1):
                if nums[j]< nums[i]:
                    res = max(res,mem[j]+1)
            mem[i]=res
        return max(mem)