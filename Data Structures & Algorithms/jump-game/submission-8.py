class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #1 brute force, top-down: try to create a new branch for every possible step i take at spot A,B ...
        # worst case time:max(nums)*len(nums), ie (max # possibilities) * max step it takes, ie when only 1 step allowed for all the other locations that are not the max numb of steps.
        # mem:n
        n=len(nums)
        if n<2:return True
        mem = [float('inf')]*len(nums)
        mem[0]=0
        # 2. O(n^2) if we go backwards and see if each spot can reach to a 'True' in the future/record the shorted num steps to get to a "true" spot
        # 3. I can hop forward and write down the shortest num steps to get there.
        #my first submission on this problem is the same logic, just only recording T/F
        # 4. I can hop backward, but i need O(n^2) since i need to check if every single cell before me can get to me
        # while i only need to hop forward by as much as my current step can take

        # for i,n in enumerate(nums):
            
        # for i in range(n):
        #     for d in range(1,nums[i] +1):
        #         if d+i>n-1:
        #             continue
        #         mem[d+i] = min(mem[d+i],mem[i]+1)
        # return mem[n-1] != float('inf')
         
        def dfs(i):
            if i >= n-1:
                return 0
            elif nums[i]==0:
                return float('inf')
            store = float('inf')
            for d in range(1,nums[i]+1):
                store = min(store,dfs(i+d)+1)
            return store
        
        return dfs(0)!=float('inf')

        

        




