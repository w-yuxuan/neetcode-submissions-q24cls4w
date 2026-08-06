class Solution:
    def jump(self, nums: List[int]) -> int:
        # if brute force out all possibilites: (# steps i can jump)^len(n)
        dp = [float('inf')]*len(nums)
        dp[-1]=0
        s=nums

        for i in range(len(s)-2,-1,-1):
            for j in range(nums[i]+1):
                if i+j<len(s):
                    dp[i] = min(dp[i],dp[i+j]+1)
        return dp[0]
