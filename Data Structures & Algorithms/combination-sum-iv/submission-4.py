class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = [0]*(target+1)
        mem[target] = 1

        for tot in range(target,-1,-1):
            for n in nums:
                if tot-n >= 0:
                    mem[tot-n] += mem[tot]
        return mem[0]