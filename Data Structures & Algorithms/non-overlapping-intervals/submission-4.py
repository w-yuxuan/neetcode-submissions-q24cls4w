class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        s = sorted(intervals,key=lambda x:x[1])
        res = 0
        n = len(s)
        cur = 0
        for new in range(1,n):
            if s[new][0]<s[cur][1]:
                res+=1
            else:
                cur =new
        return res