class Solution:
    def jump(self, nums: List[int]) -> int:
        # go backwards,store the dist from the end in place at ea step, do a for loop over the amount of fuel at each step to see what's the shortest hop from there
        #i can't recursively add the step to the closest point to that can guarantee to help me jump out 
        cp = list(nums)
        nums[-1]=0
        for i in range(len(nums)-2,-1,-1):
            curmin = float('inf')
            for n in range(1,cp[i]+1):#for all the step sizes we can take 
                if i+n>len(nums)-1: continue
                curmin = min(nums[i+n]+1,curmin)
            nums[i]=curmin
        return nums[0]




                
