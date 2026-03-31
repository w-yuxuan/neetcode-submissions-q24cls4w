class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        res = {}
        mem = defaultdict(list) # store neighbors mem[u] =[w,v]
        h = [(0,src)]
        heapq.heapify(h)

        #build mem
        for u,v,w in edges:
            mem[u].append((w,v))  

        #pop h and write to result
        while h:
            w1,v1=heapq.heappop(h)
            if v1 in res:
                continue
            res[v1]=w1
            
            #push to h
            for w2,v2 in mem[v1]:
                if v2 not in res:
                    heapq.heappush(h,(w2+w1,v2))

        #run through all n
        for i in range(n):
            if i not in res:
                res[i] =-1
        return res