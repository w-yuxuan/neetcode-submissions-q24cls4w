class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # keep popping from heap
        mem = defaultdict(list) #dst - > cost, src
        res = {} #cost,dst
        h = [(0,src)] #cost,dst
        heapq.heapify(h)

        for s,d,w in edges:
            mem[s].append((w,d))
        
        while h:
            w1,n1 = heapq.heappop(h)
            if n1 in res:
                continue
            res[n1]=w1

            for w2,n2 in mem[n1]:
                if n2 not in res:
                    heapq.heappush(h,(w1+w2,n2))

        for i in range(n):
            if i not in res:
                res[i]=-1
        return res


