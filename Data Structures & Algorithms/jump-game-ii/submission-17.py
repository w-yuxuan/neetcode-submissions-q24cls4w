class Solution:
    def jump(self, nums: List[int]) -> int:
        mem = [float('inf')] * len(nums)
        
        if len(nums) == 1:
            return 0
        mem[-1] = 0
             
        # FIX 1: Start 'i' at len(nums)-1 because mem[-1] is our only known "seed"
        for i in range(len(nums) - 1, -1, -1):
            j = i - 1
            
            # FIX 2: Only check 0 <= j in the while loop so it doesn't abort early
            while 0 <= j: 
                # Move the jump check here. If j can reach i, update mem[j].
                # If it can't, we still let j -= 1 happen to check the next one.
                if j + nums[j] >= i: 
                    mem[j] = min(mem[i] + 1, mem[j])
                
                j -= 1
                
        return mem[0]    
  

                



        # def df(i): #return min num steps so far 
            
        #     return
        # return df(0)