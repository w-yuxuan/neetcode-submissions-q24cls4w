class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mem = [0]*(target+1)
        mem[target] = 1
        
        for tot in range(target,-1,-1):
            for num in nums:
                if tot-num >= 0:
                    mem[tot-num] += mem[tot]
        return mem[0]


            