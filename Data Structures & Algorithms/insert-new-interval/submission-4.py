class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = [ ]
        new = newInterval

        while i<n and intervals[i][1]< new[0]:
            res.append(intervals[i])
            i+=1
    
        while i<n and intervals[i][1]>= new[0] and intervals[i][0]<= new[1]:
            new[0] = min(intervals[i][0],new[0])
            new[1] = max(intervals[i][1],new[1])
            
            i+=1
        res.append(new)
        

        while i<n:
            res.append(intervals[i])
            i+=1
        return res
