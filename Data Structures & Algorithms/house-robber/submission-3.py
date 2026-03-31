class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)
        c = len(nums)
        def find(j):
            if j<1:
                return nums[0]
            if j == 1:
                return max(nums[1],nums[0])
            if j < 3:
                return max(nums[1],nums[0]+nums[2])
            if cache[j]!=-1:
                return cache[j]
            cache[j] = nums[j]+max(find(j-2),find(j-3))
            
            return cache[j]
        
        return max(find(c-1),find(c-2))