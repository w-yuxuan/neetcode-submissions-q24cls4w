class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst,k): 
        temp = [float('inf')]*n
        temp[src] = 0
        res = temp.copy()

        for i in range(k+1):
            for u,v,d in flights:
                res[v] = min(res[v],temp[u]+d)
            temp = res.copy()
        return res[dst] if res[dst]!=float('inf') else -1


