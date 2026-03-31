# if i define the rest that i need to add up as c
# this needs to be a TF return, since the final result is TF and if there is any case with a True then we return it all the way up
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot%2 != 0:
            return False
        c = tot

        def dfs(i,c): # curr case sum
            #no base case to ground to 
            #if i==len(nums):
            #    return tot
            if i > len(nums)-1:
                return False
            
            if c == tot/2: return True

            # don't include
            if dfs(i+1,c)==True:
                return True    
            
            c -= nums[i]
            # include
            
            if dfs(i+1,c) == True:
                return True

            return False 
        return dfs(0,c)