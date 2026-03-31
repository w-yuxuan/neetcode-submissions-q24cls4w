class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        h = [(0,0,0)] # put the closes one to our starting node as dst
        
        mem = defaultdict(list)
        # res = {}
        length = 0

        visit = set()
        for s,d,w in edges:
            mem[s].append((w,s,d)) 
            mem[d].append((w,d,s))
        
        heapq.heapify(h)

        while h:
            w1,n1,n2 = heapq.heappop(h)
            if n2 not in visit:
                length += w1
                visit.add(n2)
            else: continue
        
            for w2,n2,n3 in mem[n2]:
                if n3 not in visit:
                    heapq.heappush(h, (w2,n2,n3))

        # return length
        return length if len(visit)==n else -1

        # for i in range(n):
        #     if i not in res:
        #         res[i]=-1
        # return res