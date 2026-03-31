class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]

        for n in nums:
            #check if curr is >0
            currSum = max(0,currSum)

            #add n to curr
            currSum += n 

            #compare curr with maxSum
            maxSum= max(currSum,maxSum)
            #return
        return maxSum
