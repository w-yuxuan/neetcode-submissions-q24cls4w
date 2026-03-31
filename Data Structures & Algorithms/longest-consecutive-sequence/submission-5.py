class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #ranking
        #bucket sort 
        count = 0
        s = set(nums)
        for i in s:
            if i-1  not in s: # start of a sequence
                cur = 1
                while i+1 in s:
                    cur += 1
                    i+=1
                count = max(count,cur)
        return count

            





