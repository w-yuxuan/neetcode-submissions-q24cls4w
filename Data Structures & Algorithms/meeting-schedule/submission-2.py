"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        if len(intervals) < 2: return True
        i = 0

        while i < len(intervals)-1:
            j = 1+i
            while j <= len(intervals)-1:
                (l1,r1) = intervals[i].start,intervals[i].end
                (l2,r2) = intervals[j].start,intervals[j].end
                if l2 < r1: return False
#                if l1 < r2: return False
                j += 1
            i+=1
        return True
             


        # while intervals:
        #     l,r = intervals.pop()
