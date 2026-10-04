class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curmin = float('inf')

        totmin = float('inf')
        n = len(nums)
        # l,r = 0,n-1
        l,r = 0,0
        tot = 0

        # for i in range(n):
        while r<n:
            tot += nums[r]
            welloff = tot - target
            
            if welloff >= 0:
                totmin = min(r-l+1, totmin)
                while l<=r and nums[l] <= welloff: # see how much we can trim some from left 
                # shouldn't adv just bc nums[r]>nums[l]
                    welloff -= nums[l]
                    tot -= nums[l]
                    l+=1
                    totmin = min(r-l+1, totmin)

            r+=1
        return totmin if totmin!= float('inf') else 0

            
