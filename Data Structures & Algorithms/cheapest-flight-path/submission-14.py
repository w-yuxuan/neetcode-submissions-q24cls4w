class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst,k): 
        # temp = [float('inf')]*n
        # temp[0] = 0
        mem,res = defaultdict(list),{}
        for u,v,d in flights:
            mem[u].append((d,v))
        h = [(0,src,0)]
        heapq.heapify(h)
        while h:
            d1,v1,k1 = heapq.heappop(h)
            # if v1 in res:
            #     continue
            if k1>k+1:
                continue
            if v1 in res and k1 >= res[v1] :
                continue
            # res[v1] = d1 # saving the shortest path so far to other places don't matter, since even though they are cheap, we don't know if their paths have too many stops to be useful in the future
            if v1==dst: # unless we see the target, which means we are under k<1 and since dijktra pops the shortest price first, this is the cheapest 
                return d1

            res[v1] = k1

            for d2,v2 in mem[v1]:
                heapq.heappush(h,(d2+d1,v2,1+k1))

            
        return -1 if dst not in res else res[dst]

