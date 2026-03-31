class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #ranking
        #bucket sort 
        count = 0
        res = {}
        mem = {}
        for i in nums:
            res[i] = res.get(i,0)+1
        for n,freq in res.items():
            cur=1
            if n-1 in res:
                continue
            while n+1 in res:
                if n+1 in mem:
                    cur += mem[n+1]
                    break
                cur +=1
                n=n+1
                mem[n] = cur
            count = max(count,cur)
        return count

            





