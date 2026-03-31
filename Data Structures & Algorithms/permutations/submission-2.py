class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            res = []
            # if i>len(nums):
            #     return
            if i == len(nums): # one step outside nums
                return [[]]

                #add to res?
            prev = helper(i+1)
            for p in prev:
                for pos in range(len(p)+1):
                    # cur = []
                    pcopy =p.copy()
                    pcopy.insert(pos,nums[i])
                    res.append(pcopy) # this is cur
            return res
        return helper(0)