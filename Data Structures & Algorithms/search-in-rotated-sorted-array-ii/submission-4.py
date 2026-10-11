class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l,r= 0, n-1
        while l<=r:
            m = (l+r)//2
            nm,nr,nl = nums[m],nums[r],nums[l]
            if target == nm or target == nl or target == nr:
                return True
            if nm < nr: # regular sorting on the right, can binary search there
                if nm <= target <= nr:
                    l = m+1
                else:
                    r = m-1
            elif nm == nr:
                r -=1
            else: # left side might be ordred/repeats, right side disordered
                if nl <= target <= nm: # left side ordered
                    r = m-1
                else:
                    l = m+1
        return False