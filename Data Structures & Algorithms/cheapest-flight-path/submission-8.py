class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mem=defaultdict(list)
        res,temp = [float('inf')]*n, [float('inf')]*n
        for u,v,d in flights:
            mem[u].append((d,v)) 
        s = src
        cost = 0
        q = deque([[0,src]])
        lev = 0
        while q and lev <k+1:
            n = len(q)
            for i in range(n):
                cost,s = q.popleft()
                for cost2,e in mem[s]:
                    if temp[e] >(cost+cost2):
                        temp[e] = cost+cost2
                        q.append([temp[e],e])  
            lev +=1
        return temp[dst] if temp[dst]!=float('inf') else -1
            

            
            #     for cost2,e2 in mem[e]:
            #         res[e2] = min(cost2+cost1,temp[e])
            # s = e
