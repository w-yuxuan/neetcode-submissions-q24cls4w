class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #initalize subest
        subset,curr = [],[]

        def helper(i,nums,subset,curr):
            if i > len(nums)-1:
                subset.append(curr.copy())
                return subset
            
            curr.append(nums[i])
            helper(i+1,nums,subset,curr)
            curr.pop()

            helper(i+1,nums,subset,curr)

        helper(0,nums,subset,curr)

        return subset
            