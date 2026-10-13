class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mem = defaultdict(int)
        n = len(nums)
        goal = n//3

        for i in range(n):
            mem[nums[i]]+=1
        
        return [num  for num,val in mem.items() if val > goal]