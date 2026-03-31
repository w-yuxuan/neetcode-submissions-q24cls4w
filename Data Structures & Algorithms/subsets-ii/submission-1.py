class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # initalize
        nums.sort()
        curr, sub = [ ], [ ]

        def dfs(i,curr):
            if i > len(nums)-1:
                sub.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()

            while i < len(nums)-1 and nums[i+1] == nums[i] :
                i+=1
            dfs(i+1,curr)
        
        dfs(0,curr)
        return sub
