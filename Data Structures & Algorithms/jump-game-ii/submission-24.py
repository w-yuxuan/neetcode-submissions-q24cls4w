class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n = len(nums)
        steps = 0
        l , r = 0,0 #the cur steps hopping range
        cur = 0
        furthest = 0
        while r <= n-2:
            while cur <=r:
                furthest = max(cur + nums[cur],furthest)
                # if furthest >= n-1:
                #     return steps+1
                cur +=1
            l = r+1
            r = furthest
            steps +=1
        return steps
        

            
            



