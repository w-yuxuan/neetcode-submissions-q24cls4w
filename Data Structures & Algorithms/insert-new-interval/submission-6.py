class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: 
        res = []
        new = newInterval
        for i in range(len(intervals)):
            if new[1]< intervals[i][0] : # there will be no new interfereing with me later, so just add all intervals behind this and return
                res.append(new )
                return res+intervals[i:]
            if intervals[i][1]< new[0]: # don't return bc i ccould meet  the new later
                res.append(intervals[i])
                # return res
            else:
                new[0] = min(intervals[i][0], new[0])
                new[1] = max(intervals[i][1], new[1])
        res.append(new) # if i haven't returned that means i have the new at the end of the returned list 
        return res
            

