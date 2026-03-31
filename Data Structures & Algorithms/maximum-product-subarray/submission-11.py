class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = 1
        gMax = gMin = nums[0]
        for i in range(len(nums)):
            # clean add floor 
            if nums[i]== 0 :
                curMax = curMin = 1
                gMax = max(gMax, 0)
                continue
            temp = curMax 
            curMax = max(nums[i],curMax*nums[i],curMin*nums[i]) # either continue from prev or start over
            curMin = min(nums[i],curMin*nums[i],temp*nums[i])
            gMax = max(curMax,curMin,gMax)
        return gMax
            