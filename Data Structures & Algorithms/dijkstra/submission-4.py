class Solution:
    def shortestPath(self,n:int,edges:[list[list[int]]],src):
        # each time i pop i add the neighbors to the list 
        res = {} # maps node to shortest
        mem = [] #[src:dst]
        h = [(0,src)] 
        heapq.heapify(h)

        mem = defaultdict(list)
        
        for s,d,w in edges:
            mem[s].append((d,w)) 
        
        while h:
            w1,n1 = heapq.heappop(h)
            if n1 in res:
                continue
            res[n1] = w1

            for n2,w2 in mem[n1]:
                if n2 not in res:# check if forms a loop
                    heapq.heappush(h,(w2+w1,n2))
        for i in range(n):
            if i not in res:
                res[i] = -1
        return res