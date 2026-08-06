class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        glob = set()
        # h = deque()

        mem = defaultdict(list)
        for u,v in edges:
            mem[u].append(v)
            mem[v].append(u)

        def dfs(i):
            h = deque([i])
            # heapq.heapify(h)
            
            been  = set()

            while h:
                u1 = h.popleft()
                if u1 in been:
                    continue
                been.add(u1)

                for u2 in mem[u1]:
                    if u2 not in been:
                        h.append(u2)
            return been
        

        for i in range(n):
            if i not in glob:
                for j in dfs(i):
                    glob.add(j)
                count+=1
                
        return count


                
            
            
            


        
        
