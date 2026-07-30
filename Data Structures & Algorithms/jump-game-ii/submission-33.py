class Solution:
    def jump(self, nums: List[int]) -> int:
        # if len(nums) <= 1: return 0
        l=r=0 # l and r for cur segment 
        step = 0
        
        while r < len(nums)-1:
            far = 0 
            for i in range(l,r+1):
                far = max(far,i+nums[i])
            l=r+1
            r = far
            
            step+=1
        return step