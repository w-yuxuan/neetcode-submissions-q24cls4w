class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)
        
        # cost: n log n + K
        # for x,y in points:
        #     dist = x**2+y**2
        #     heapq.heappush(h,[dist,x,y])

        n = len(points)
        if n<=k:
            return points
        for i in range(n):
            x,y = points[i]
            dist = x**2+y**2 ## need to be righ under for loop
            if i <k:
                heapq.heappush(h,[-dist,x,y])
            elif h[0][0] < -dist:
                heapq.heappop(h)
                heapq.heappush(h,[-dist,x,y])
        res = []
        for a,b,c in h:
            res.append([b,c])
        return res
        # return [b,c] for a,b,c in h

            