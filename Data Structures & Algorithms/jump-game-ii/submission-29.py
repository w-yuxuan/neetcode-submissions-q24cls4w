class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0   # FIX 1: Handle array of length 1
        
        l, r = 0, 0 
        step = 0
        stop = 0                      # FIX 2: Start stop at 0, not nums[0]
        
        while True:
            # r = stop                <-- REMOVED: Don't update r before the level is processed
            while l <= r:             # FIX 3: Change < to <= to include the end of the current level
                stop = max(stop, nums[l] + l)
                if stop >= len(nums) - 1:
                    return step + 1
                l += 1
            
            r = stop                  # FIX 4: Update r here, after finishing the current level
            step += 1
            