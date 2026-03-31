class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        def help(i):
            res = []
            if i == len(nums):
                return [[]]
            prev = help(i+1)
            for p in prev:
                for pos in range(len(p)+1):
                    pcopy = p.copy() # only a valid perm to add to result if 
                    pcopy.insert(pos,nums[i])
                    
                    res.append(pcopy)
                    if pos <= len(p)-1 and p[pos]==nums[i]:
                        break
            return res
        return help(0)