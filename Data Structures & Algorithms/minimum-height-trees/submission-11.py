class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nei,cnt = defaultdict(list),defaultdict(int)
        for s,e in edges:
            nei[s].append(e)
            nei[e].append(s)
            cnt[s]+=1
            cnt[e]+=1
        
        layer = deque()
        for node in range(n):
            if cnt[node]==1:
                layer.append(node)
        full = [x for x in range(n)] 

        while len(full)>2:
            # trim this layer
            for _ in range(len(layer)):
                node = layer.popleft()
                full.remove(node)
                for n1 in nei[node]:
                    cnt[n1]-=1
                    if cnt[n1]==1:
                        layer.append(n1)
        return full

                