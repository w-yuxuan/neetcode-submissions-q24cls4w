class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        def help(i):
            if i == len(nums):
                return [[]]
            res = []
            prev = help(i+1)
            for p in prev:
                for pos in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(pos, nums[i]) # Always insert
                    res.append(pcopy)
                    
                    # FIX: Stop if we just placed nums[i] next to an identical number.
                    # We check 'p' (the original list without the new number).
                    if pos < len(p) and p[pos] == nums[i]:
                        break 
            return res
        return help(0)