class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        res = {}
        tot =0
        mem = defaultdict(list)
        for u,v,w in edges:
            mem[u].append((w,v))
            mem[v].append((w,u))
        
        h = [(0,0)]
        heapq.heapify(h)
        while h:
            w1,v1  = heapq.heappop(h)
            if v1 in res:
                continue
            res[v1] = w1
            tot += w1

            for w2,v2 in mem[v1]:
                if v2 not in res:
                    heapq.heappush(h,(w2,v2))

        return sum(res.values()) if len(res) == n else -1
        