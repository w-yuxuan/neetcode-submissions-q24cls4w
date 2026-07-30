class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mem = defaultdict(list)
        for u,v,t in times:
            mem[u].append((t,v))
        res = {}
        h = [(0,k)]
        heapq.heapify(h)

        while h:
            t1,v1 = heapq.heappop(h)
            if v1 in res:
                continue
            res[v1] = t1

            for t2,v2 in mem[v1]:
                if v2 not in res:
                    heapq.heappush(h,(t1+t2,v2))
        if len(res.keys())<n:
            return -1
        return max(res.values())

            