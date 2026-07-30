class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        res = {}
        mem = defaultdict(list)
        for u,v,w in edges:
            mem[u].append((w,v))
        
        h = [(0,src)]
        heapq.heapify(h)
        while h:
            w1,v1 = heapq.heappop(h)
            if v1 in res:
                continue
            res[v1] = w1

            for w2,v2 in mem[v1]:
                if v2 not in res:
                    heapq.heappush(h,(w1+w2,v2))
        
        for i in range(n):
            if i not in res:
                res[i] = -1
        return res
        