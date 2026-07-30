class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        h = []
        heapq.heapify(h)
        dp = defaultdict(list)

        for u,v,w in edges:
            dp[u].append((w,v))
        
        res = {}
        # res[src]=0
        heapq.heappush(h,(0,src))

        while h:
            w1,v1 = heapq.heappop(h)
            if v1 in res:
                continue
            res[v1] = w1

            for w2,v2 in dp[v1]:
                if v2 not in res:
                    heapq.heappush(h,(w1+w2,v2))
        
        # if len(res) < n:
        #     return -1
        # return max(res.values())
            
        for i in range(n):
            if i not in res:
                res[i]=-1
        return res
