class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset , curr = [],[]
        nums.sort()
        
        def dfs(i):
            if i>len(nums)-1:
                subset.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()

            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
                # instead of returning subset.append(curr.copy()) since there can later be non repeating numbers, you just want to skip over repeated ones and not do dfs on those indicies so that they won't end up in that braches' answer when we reach the base case
            dfs(i+1)

        dfs(0)
        return subset



