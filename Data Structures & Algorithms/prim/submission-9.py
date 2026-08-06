class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        res = {}
        mem = defaultdict(list)
        for u,v,w in edges:
            mem[u].append((w,v))
            mem[v].append((w,u))
        h = [(0,0)]
        heapq.heapify(h)
        while h:
            w1,u1=heapq.heappop(h)
            if u1 in res:
                continue
            else:
                res[u1] = w1

            for w2,u2 in mem[u1]:
                if u2 not in res:
                    heapq.heappush(h,(w2,u2))
        if len(res)<n:
            return -1
        return sum(res.values())
            