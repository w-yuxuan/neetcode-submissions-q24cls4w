class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # keep popping from heap
        mem = defaultdict(list) #dst - > cost, src
        res = set()
        h = [(0,0)] #cost,dst
        heapq.heapify(h)
        l = 0

        for s,d,w in edges:
            mem[s].append((w,d))
            mem[d].append((w,s))
        
        while h:
            w1,n1 = heapq.heappop(h)
            if n1 in res:
                continue
            l+=w1
            res.add(n1)

            for w2,n2 in mem[n1]:
                if n2 not in res:
                    heapq.heappush(h,(w2,n2))

        if len(res)<n:
            return -1
        else:
            return l


 