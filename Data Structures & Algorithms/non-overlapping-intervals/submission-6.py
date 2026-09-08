class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res = 0
        n = len(intervals)
        cur = 0
        for new in range(1,n):
            if intervals[new][0]<intervals[cur][1]:
                res+=1
            else:
                cur =new
        return res