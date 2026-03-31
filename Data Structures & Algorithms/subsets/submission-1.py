class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #initalize subest
        subset,curr = [],[]

        def helper(i):
            if i > len(nums)-1:
                subset.append(curr.copy())
                return subset
            
            curr.append(nums[i])
            helper(i+1)
            curr.pop()

            helper(i+1)

        helper(0)

        return subset
            