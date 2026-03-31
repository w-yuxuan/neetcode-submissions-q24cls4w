class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mem = defaultdict(list) #mem[src]=(cost,dst)
        res = {} #(cost,dst)
        h = [(0,k)] #(cost,dst)
        heapq.heapify(h)

        for ui,vi,ti in times:
            mem[ui].append((ti,vi))
        
        while h:
            cost,n1 = heapq.heappop(h)
            if n1 in res:
                continue
            res[n1] = cost

            for cost2,n2 in mem[n1]:
                if n2 not in res:
                    heapq.heappush(h,(cost+cost2,n2))
        
        for num in range(1,n+1):
            if num not in res:
                return -1
        return max(res[x] for x in range(1,n+1))