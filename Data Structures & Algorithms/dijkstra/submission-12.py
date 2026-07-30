class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        mem = defaultdict(list)
        for u,v,w in edges:
            mem[u].append((v,w))

        h = [(0,src)]
        heapq.heapify(h)

        res = {}
        # res[src] = 0
        while h:
            w1,v1 = heapq.heappop(h)
            if v1 in res:
                continue
            res[v1] = w1

            for v2,w2 in mem[v1]:
                if v2 not in res:
                    heapq.heappush(h,(w2+w1,v2))

        for e in range(n):
            if e not in res:
                res[e]=-1
        return res




