class Solution:
    def rob(self, nums: List[int]) -> int:
        c = len(nums)
        if len(nums)<2:
            return nums[0]
        if c>2:
            nums[c-3] = nums [c-3] + nums[c-1]
        
        for i in range(c-4,-1,-1): # last value is 0 so we updated the full list
            nums[i] += max(nums[i+2],nums[i+3])
        return max(nums[1],nums[0]) # the [2] is same as [0] case except one more house added, [3] as [1] case 
        #[4] is as [0] case