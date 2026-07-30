class Solution:
    def jump(self, nums: List[int]) -> int:
        curmax = nums[0]
        nextmax=0
        jump = 1
        i = 0
        if len(nums)==1:
            return 0
            
        while True:
            
            while i<= curmax:
                if i >= len(nums)-1:
                    return jump
                nextmax = max(i+nums[i],nextmax)
                # if nextmax >= len(nums)-1:
                #     return jump+1
                i+=1
                # if i > curmax:
                #     return False  

            jump+=1
            curmax = nextmax
            nextmax = 0

        return jump


