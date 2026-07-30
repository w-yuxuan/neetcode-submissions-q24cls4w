from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        mem = defaultdict(int)
        for t in tasks:
            mem[t] = mem[t]-1 # turn into negative
                # or mem = {} mem[t] = mem.get(t,0)+1
        # store(#timesLeft,#secToWait)
        h1 , q = list(mem.values()),deque() # not [mem.values()] to prevent [ []]

        heapq.heapify(h1)
                
        # for i in mem.values():
        while h1 or q: # always check h2 first and move any ready ones to h1. Always pop h1
            if q:
                if q[0][0]<=res: # keep < not == since there can be many that can be poped but we can pop 1 at each time
                    n2,v2 = q.popleft()
                    heapq.heappush(h1,v2)

            if h1:
                v1 = heapq.heappop(h1)
                if v1+1 < 0:
                    q.append([res+n+1,v1+1]) 
            res+=1
        return res             



