class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = 1
        gMax = nums[0]
        for i in range(len(nums)):
            # clear add floor
            if nums[i]==0:
                curMax = curMin =1
                gMax = max(gMax,0)
                continue 
            temp = curMax 
            curMax = max(curMax*nums[i],curMin*nums[i],nums[i])
            curMin = min(temp*nums[i],curMin*nums[i],nums[i])
            gMax = max(gMax,curMax)
        return gMax
