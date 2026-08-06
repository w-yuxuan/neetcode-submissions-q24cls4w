class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwd = [1]*len(nums)
        bk = [1]*len(nums)
        res = [1]*len(nums)

        p = 1
        for i in range(len(nums)):
            p=p*nums[i]
            fwd[i]=p
        p = 1
        for i in range(len(nums)-1,-1,-1):
            p*=nums[i]
            bk[i]=p
        
        for i in range(len(nums)):
            if i == 0:
                f = 1
            else: f = fwd[i-1]
            if i == len(nums)-1:
                b = 1
            else: b = bk[i+1]
            res[i] = f*b
        return res

