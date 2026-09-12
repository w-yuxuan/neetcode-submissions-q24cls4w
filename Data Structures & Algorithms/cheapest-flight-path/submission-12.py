class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        temp = [float('inf')]*n
        temp[src] = 0
        res = temp.copy()
        for i in range(k+1):
            # for j in range(len(temp)):
            #     if temp[j]==float('inf'):
            #         continue
            for u,v,d in flights:
                res[v] = min(temp[u]+d,res[v])
            temp = res.copy()
        return res[dst] if res[dst]!= float('inf') else -1 
            
            

        