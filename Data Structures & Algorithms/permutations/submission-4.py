class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #base case
        def permu(i,nums):
            if i==len(nums):
                return [[]]
            resPerm = []
            permutations = permu(i+1,nums)
            for p in permutations:
                for j in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(j,nums[i])
                    resPerm.append(pcopy)
            return resPerm
        return permu(0,nums)


            
        