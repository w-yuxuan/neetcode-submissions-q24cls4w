"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        maxday = 0
        day =1
        if len(intervals) >= 1:
            maxday =  1
        st = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        j=1
        k=0
        while j <= len(st)-1:
            # if j == 1: k = j-1
            if st[j] < end[k]:
                day += 1
                j += 1
                maxday = max(maxday,day)
            else:
                k+=1
                day -=1
        return maxday