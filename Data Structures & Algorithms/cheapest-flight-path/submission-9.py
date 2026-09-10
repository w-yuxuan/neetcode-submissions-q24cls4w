class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        temp,res = [float('inf')]*n, [float('inf')]*n 
        mem = defaultdict(list)
        for u,v,d in flights:
            mem[u].append((d,v))

        temp[src]=0
        while k>=0:

            k-=1
            for i in range(len(temp)):
                if temp[i] !=float('inf'):
                    for d2,v2 in mem[i]:
                        res[v2] = min(res[v2],temp[i]+d2)
            temp = res.copy()
        return res[dst] if res[dst]!=float('inf') else -1
