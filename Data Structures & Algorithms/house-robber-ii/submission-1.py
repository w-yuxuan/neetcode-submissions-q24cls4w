class Solution:
    def rob(self, nums: List[int]) -> int:
        c = len(nums)-1
        def run(nums):
            if len(nums) < 2:
                return nums[0]
            if len(nums)>2:
                nums[c-3]=nums[c-3]+nums[c-1]
            for i in range(c-4,-1,-1):
                nums[i]+=max(nums[i+2],nums[i+3])
            return max(nums[0],nums[1])
        if len(nums) < 2:
            return nums[0]
        else: return max(run(nums[:-1]),run(nums[1:]))