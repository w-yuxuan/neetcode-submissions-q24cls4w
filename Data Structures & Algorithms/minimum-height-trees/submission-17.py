class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nei,cnt = defaultdict(list),defaultdict(int)
        res = []
        if n==1:
            return [0]
        for s,e in edges:
            nei[s].append(e)
            nei[e].append(s)
            cnt[s]+=1
            cnt[e]+=1
        full = [x for x in range(n)]
        layer = deque()
        for node in range(n):
            if cnt[node]==1:
                layer.append(node)

        while len(full)>2:
            #pop off, update neighbor's cnt
            for _ in range(len(layer)):
                node = layer.popleft()
                for neighbor in nei[node]:
                    cnt[neighbor]-=1
                    if cnt[neighbor]==1:
                        layer.append(neighbor)
                full.remove(node)
            
            # for node in layer:
            #     if node in full:
            #         full.remove(node)
            
        return full
                

        

        
        


                