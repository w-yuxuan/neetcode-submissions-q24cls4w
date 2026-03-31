class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #corrections

        maxSum = nums[0]
        L = 0 
        currSum = 0

        #next loop sets R

        
        for R in range(len(nums)):
        #loop to start working at index 0 since it's range(1)
        
            #currSum = sum(nums[L:R+1])
            #too expensive above
            currSum += nums[R]
        
        
         
            maxSum = max(currSum,maxSum)

            #reset to 0
            if currSum <= 0:
                L = R
                currSum = 0
        return maxSum