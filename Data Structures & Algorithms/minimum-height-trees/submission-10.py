class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nei,cnt = defaultdict(list),defaultdict(int)
        for s,f in edges:
            nei[s].append(f)
            nei[f].append(s)
            cnt[s]+=1
            cnt[f]+=1
        visit = set()
        full = [x for x in range(n)]
        full = set(full)
        # j = 1
        layer = deque()
        for node in range(n): # better than going throuig hthe edges since there are 2 nodes to check per edge
            if node in full and cnt[node]==1: 
                layer.append(node)


        while len(full) > 2:
            # for node in full: # better than going throuig hthe edges since there are 2 nodes to check per edge
            #     if node not in visit and cnt[node]==1:
            for _ in range(len(layer)):
                node = layer.popleft()
                #cut it and add to res
                full.discard(node)
                for p in nei[node]:
                    if p in full:
                        cnt[p]-=1 
                        if cnt[p]==1:
                            layer.append(p)
                            
        return list(full)


            



            
                
            

                    

            
            
