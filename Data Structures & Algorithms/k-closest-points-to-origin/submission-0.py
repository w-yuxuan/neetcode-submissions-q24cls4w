import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #costs n to build a hash
        h = []
        if not points:
            return NameError
        for point in points: 
            dist = point[0]**2 + point[1]**2
            h.append((dist,point)) # make sure double (()) to store a pair

        find = heapq.nsmallest(k,h) #O(nlogK)
        res =[]
        for _,point in find: #O(K)
            res.append(point) #o(K)
        return res
