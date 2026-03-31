class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stop = 0
        for i,n in enumerate(nums):
            stop =max(stop-1,n) # two choices: compare previous max - 1 hop with current refuel
            #stop+=n # no stop doesn't accumulate
            if not stop and i<len(nums)-1: # allowed to run out of fuel at very last step
                return False
        return True