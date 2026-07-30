class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        l=r=0 # l and r for cur segment 
        stop = 0
        step = 0
        
        while r < len(nums)-1:
            while l<=r:
                stop = max(stop,l+nums[l])
                l+=1
            r=stop
            step +=1

        return step

