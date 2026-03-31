class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        goal = total/2
        c = total

        if total%2 != 0:
            return False
        
        def dfs(i,c):
            if i > len(nums)-1:
                return False
            
            if c == goal:
                return True
            
            #don't inlcude
            if dfs(i+1,c) == True:
                return True
            
            c -= nums[i]
            #include
            if dfs(i+1,c) == True:
                return True

            return False
        return dfs(0,c)
            

            
            
