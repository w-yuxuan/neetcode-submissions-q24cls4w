class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [0]*(len(nums))
        mem[0]=1
        for i in range(1,len(nums)):
            res= 1
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res,1+mem[j])
            mem[i]=res
        return max(mem)