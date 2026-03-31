class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       # O(1) means we have a storage << n/2,
       # i can sort and then use a single storage: nlogn and 1 cost/mem
       # i can iterate through all but then need O(n) storage
       s = nums[0]
       f = nums[nums[0]]

       def dfs(f,s):
        f = 0
        while True:
            if s == f:
                return s
            else: 
                s = nums[s]
                f = nums[f]

       while f and s:
        if s == f:
            return dfs(f,s)
        else: 
            s = nums[s]
            f = nums[nums[f]]
        
        