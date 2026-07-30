class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0, 0
        lev = 0
        while True:
            for i in range(l,r+1):
                if i >= len(nums)-1:
                    return lev
                r = max(r,i+nums[i])
            l = i+1
            lev+=1

