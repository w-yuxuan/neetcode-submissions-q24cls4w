import math
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # calculate pairwise distances: cost n^2
        # then graph problem cost v+e, n verticies, n-1 edges
        n = len(points)
        mem ,res = defaultdict(list),{}
        for i in range(n):
            for j in range(i+1,n):
                d = (abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]))
                mem[tuple(points[i])].append((d,tuple(points[j])))
                mem[tuple(points[j])].append((d,tuple(points[i])))
        
        h = []
        heapq.heapify(h)
        h.append((0,tuple(points[0])))

        while h:
            w1,v1 = heapq.heappop(h)
            if v1 in res:
                continue
            res[v1] = w1
            
            for w2,v2 in mem[v1]:
                if v2 not in res:
                    heapq.heappush(h,(w2,v2))
        tot = 0
        for dist in res.values():
            tot+=dist
        
        return tot