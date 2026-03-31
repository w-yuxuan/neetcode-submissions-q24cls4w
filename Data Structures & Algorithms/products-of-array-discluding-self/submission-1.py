class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        prefix =1
        for i in range(len(nums)):
            
            res[i] = prefix
            prefix *= nums[i]
        # for i,n in enumerate(nums[::-1])
        # for i in range(0,len(nums),-1):
        postfix = 1
        for i in range(-1,-len(nums)-1,-1):
            
            res[i] *=postfix
            postfix *= nums[i]
        return res
        