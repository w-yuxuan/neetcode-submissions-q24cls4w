class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        l = 0
        r=1 
        #err: r means the furthest the current step can go , l is the pointer we use to go through ever spot
        # r means the furthest the NEXT step can go , l is the pointer for the bdnry where the cur step can't go 
        
        cur = 0
        step = 1

        while True: # ea iter means 1 step
            furthest = 0 
            # while r <= len(nums): #
            while cur < r: # loop to advance cur 
                furthest = max(cur+nums[cur] , furthest) # update r
                cur +=1
                if furthest >= len(nums)-1: # if cur step can reach end 
                    return step 
            step +=1
            l=r
            r=furthest+1

        
