class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tot=0
        n = len(nums)
        l,r = 0,0
        best = float('inf')
        while r < n: # ea time right side forward, left side try to get as close as it ca 
            tot+=nums[r]
            extra = tot - target

            while l<=r and extra >= nums[l]: 
                tot -= nums[l]
                extra -= nums[l]
                l+=1
            if extra >=0 :
                best = min(best,r-l+1)            
            r+=1
        return best if best!= float('inf') else 0