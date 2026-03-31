class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        h = [(0,0)] #w,dst
        mem = defaultdict(list) # src, w,dst
        res = set() # w,dst
        l=0

        heapq.heapify(h)
        for s,d,w in edges:
            mem[s].append((w,d))
            mem[d].append((w,s))
        while h:
            w1,n1 = heapq.heappop(h)
            if n1 in res:
                continue
            res.add(n1)
            l+=w1

            for w2,n2 in mem[n1]:
                if n2 not in res:
                    heapq.heappush(h,(w2,n2))

        return l if len(res)==n else -1                

            
        


 