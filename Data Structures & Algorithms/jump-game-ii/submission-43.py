class Solution:
    def jump(self, nums: List[int]) -> int:
        # step based apporach: calculating the index we can furthest go for each step
        # dp breaks q down to sub q: calculates the min steps needed to ge tto each position.  since the goal is to find the smallest # to get to the end, not each intermediate step, this is slower
        if len(nums)==1:
            return 0
        step = 0
        l,r  = 0,0
        far = 0
        while True:
        # while r < len(nums)-1:
            for i in range(l,r+1):
                far = max(far,nums[i]+i)
            
            l = r
            r = far
            step +=1
            if r >= len(nums)-1:
                return step
            


