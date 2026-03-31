class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # reshine's doubts:
        # if i'm going fwd, how do i know what's the farthest i can jump to on that branch if i havne't reached the end?
        # if i'm going backward, i would need to visit each spot and write where i can
        stop = 0
        # note down the furthest we can jumpt to. return False if stop = i
        for i,n in enumerate(nums):
            stop = max(stop,n+i)
            if stop<=i and i!=len(nums)-1:
                return False
        return True

        

        




