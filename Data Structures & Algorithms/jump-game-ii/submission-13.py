class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        farthest=0
        r=l=0
        while r<len(nums)-1: #loop over each level
            farthest = max(farthest,r+nums[r]) #only repeated up here bc we need to this for the first number
            r=farthest
            while l<=r<=len(nums)-1:# loop over all elemnts in this level to update farthest
                farthest = max(farthest,l+nums[l])
                l+=1
            res +=1
            #l+=1 # go from l=r to l=cur_r+1
            # r = farthest
        return res





            
            
        




                
