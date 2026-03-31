class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        h = [(0,src)]
        mem = defaultdict(list)
        res = {}

        for s,d,w in edges:
            mem[s].append((w,d))
        
        heapq.heapify(h)

        while h:
            w1,n1 = heapq.heappop(h)
            if n1 not in res:
                res[n1]=w1
            else: continue
        
            for w2,n2 in mem[n1]:
                if n2 not in res:
                    heapq.heappush(h, (w1+w2,n2))
        for i in range(n):
            if i not in res:
                res[i]=-1
        return res