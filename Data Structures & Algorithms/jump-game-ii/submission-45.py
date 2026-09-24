class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        step = 0
        l = r = 0
        n = len(nums)
        far = nums[0]
        while l<=r<n:
            for i in range(l,r+1):
                far= max(far,i+nums[i])
                if far>=n-1:
                    return step+1
            step +=1
            l=r+1
            r = far
        
            


