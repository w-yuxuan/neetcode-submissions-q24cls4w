class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
  

        maxSum = nums[0]
        currSum = 0

        #if i only have 1 value then?
        # what you have it to make sure the nums[0 ] gets compared to 0
        #verify you can return 0 for [-7]?
        
        for n in nums:
            # throw out all previous val if goes -
            currSum = max(0,currSum) 
            currSum += n 
            #above two lines fixes the imcomplete logic in my own try

            maxSum = max(maxSum,currSum)
        return maxSum