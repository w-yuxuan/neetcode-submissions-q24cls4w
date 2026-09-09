class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res,mem = {},defaultdict(list)
        for u,v,d in flights:
            mem[u].append((d,v))
        h =[(0,src,0)]
        heapq.heapify(h)

        while h:
            d1,v1,k1 = heapq.heappop(h)
            if k1>k+1:
                continue
            if v1 in res and res[v1]<=k1:
                continue
            res[v1]=k1
            
            if v1 == dst:
                return d1
            
            for d2,v2 in mem[v1]:
                heapq.heappush(h,(d1+d2,v2,k1+1))
        return -1
        