#need to improve
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        stp=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= goal: # call hop
                stp+=1
                goal = i
        return True if goal==0 else False        
        #return stp


