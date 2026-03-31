class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #ranking
        #bucket sort 
        count = 0
        res = {}
        for i in nums:
            res[i] = res.get(i,0)+1
        for n,freq in res.items():
            cur=1
            while n+1 in res:
                cur +=1
                n=n+1
            count = max(count,cur)
        return count

            





