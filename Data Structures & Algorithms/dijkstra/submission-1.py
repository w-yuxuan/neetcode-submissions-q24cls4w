class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # 
        shortest = {} #[dst:cheapest cost]
        adj = defaultdict(list) #[source:dst]
        
        h = [[0,src]]
        for s,d,w in edges:
            adj[s].append((d,w))
        
        heapq.heapify(h)
        while h:
            w1,n1 = heapq.heappop(h)
            #if like the first src, if we don't have the cost to reach there, add it 
            if n1 in shortest:
                continue
            shortest[n1] = w1 
            
            for n2,w2 in adj[n1]:#push current closet path to all neighbors'  heap
                # cost = w2 + w1
                # adj[n2] = min(cost,adj[n2])
                # why only push it on when node hasn't been visited?
                if n2 not in shortest: #only add to heap to explore later if I never popped a tuple
                # with that node from the heap, ie haven't concluded on the closest path to n2 yet.  prevent circles, 
                    heapq.heappush(h,(w1+w2,n2)) # not (h,w+w)
            #only when we pop a (s,d,w), we add it to the result, ie "shortest"

        for nn in range(n):
            if nn not in shortest:
                shortest[nn] = -1
        
        return shortest