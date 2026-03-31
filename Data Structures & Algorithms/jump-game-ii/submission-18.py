class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        mem = [float('inf')] * n
        mem[0] = 0  # FIX 1: Start at index 0 with 0 jumps
             
        # FIX 2: Iterate forward. Stand at 'i' and look at where you can go.
        for i in range(n):
            # For every position 'i', look at all possible landing spots 'j'
            max_jump = min(i + nums[i], n - 1)
            
            for j in range(i + 1, max_jump + 1):
                # Update the landing spot with current jumps + 1
                if mem[i] + 1 < mem[j]:
                    mem[j] = mem[i] + 1
                    
        return mem[n-1]